import copy
import json
import math
import random
from datetime import datetime, timedelta
from typing import List

from src.core.tabu_algorithm.src.common import generate_uuid, MIN_DISTANCE, weekday_count, text_to_vector, get_cosine, \
    MIN_COSINE_SIMILARITY, string_to_datetime, minutes_between_two_date
from src.core.tabu_algorithm.src.models.individual import Individual
from src.core.tabu_algorithm.src.models.job import Job
from src.core.tabu_algorithm.src.models.schedule import Schedule
from src.core.tabu_algorithm.src.models.time_slot import TimeSlot, BreakingTimeSlot, WorkingTimeSlot
from src.core.tabu_algorithm.src.validate import validate_input_data

LATENESS_MAX: float = math.inf


def schedule_generate(start_time, end_time):
    schedule = Schedule(start_time=start_time, end_time=end_time)
    return schedule


def add_breaking_time_slots(schedule: Schedule, time_slots: List[BreakingTimeSlot]):
    start_time_slot = TimeSlot(id=generate_uuid(), start_time=schedule.start_time, end_time=schedule.start_time)
    end_time_slot = TimeSlot(id=generate_uuid(), start_time=schedule.end_time, end_time=schedule.end_time)
    schedule.time_slots.append(start_time_slot)
    schedule.time_slots.append(end_time_slot)
    schedule.time_slots += time_slots
    return schedule


def add_fixed_time_working_time_slots(schedule: Schedule, jobs: List[Job]):
    # print('add_fixed_time_working_time_slots')
    for job in jobs:
        if job.flextime == 0:
            w = WorkingTimeSlot(id=generate_uuid(), start_time=job.early_start_time,
                                end_time=job.late_finish_time, job=job, remaining_time=0)
            schedule.time_slots.append(w)
    return schedule


def filter_list_time_slots(time_slots: List[TimeSlot], min_distance=MIN_DISTANCE):
    # for x in time_slots:
    # print(type(x), x)
    time_slots.sort(key=lambda x: x.start_time)
    filter_time_slots = [time_slots[0]]
    for i in range(1, len(time_slots)):
        if int((time_slots[i].start_time - filter_time_slots[-1].end_time).total_seconds() / 60) <= min_distance:
            filter_time_slots[-1].end_time = time_slots[i].end_time
        else:
            filter_time_slots.append(time_slots[i])
    return filter_time_slots


def add_reused_working_time_slots(schedule: Schedule, reused_working_time_slots: List[WorkingTimeSlot],
                                  jobs: List[Job]):
    # print('add_reused_working_time_slots')
    timeline = schedule.time_slots.copy()
    start_time_reused_job = []
    timeline = filter_list_time_slots(timeline)
    flextime_jobs = [job for job in jobs if job.flextime == 1]
    weekdays = weekday_count(schedule.start_time, schedule.end_time)
    for job in flextime_jobs:
        for t in reused_working_time_slots:
            job_name = text_to_vector(job.name.lower())
            recent_job_name = text_to_vector(t.job.name.lower())
            cosine_similar = get_cosine(job_name, recent_job_name)
            if cosine_similar >= MIN_COSINE_SIMILARITY:
                # print(job.__dict__)
                # print('______')
                reuse_start_time = t.start_time.strftime('%H:%M:%S')
                reuse_weekday = weekdays[f"{t.start_time.strftime('%A')}"]
                reuse_datetime = []
                for w in reuse_weekday:
                    reuse_date = w.strftime('%Y-%m-%d')
                    x = reuse_date + ' ' + reuse_start_time
                    reuse_datetime.append(string_to_datetime(x))
                # print(reuse_datetime, "reuse_datetime")
                for i in range(len(reuse_datetime)):
                    valid_reuse_datetime, timeline_index = check_valid_reuse_datetime(
                        reuse_datetime[i], timeline)
                    # print(valid_reuse_datetime, timeline_index,
                    #       "valid_reuse_datetime, timeline_index")
                    if not valid_reuse_datetime:
                        i += 1
                    else:
                        # print(reuse_datetime[i], "reuse_datetime")
                        timeline, start_time_reused_job = add_job_to_timeline(
                            timeline, start_time_reused_job, timeline_index, job, reuse_datetime[i])
    return timeline, start_time_reused_job


def check_valid_reuse_datetime(checked_datetime: datetime, timeline: List[TimeSlot]):
    for i in range(len(timeline) - 1):
        if timeline[i].end_time <= checked_datetime < timeline[i + 1].start_time:
            return True, i
    return False, i


def add_job_to_timeline(timeline: List[TimeSlot], start_time_reused_job: List[Job], timeline_index: int, job: Job,
                        reuse_datetime: datetime):
    temp_timeline = timeline.copy()
    updated_start_time_reused_job = start_time_reused_job
    if reuse_datetime < job.early_start_time:
        return temp_timeline
    else:
        temp_timeline_index = 0
        if temp_timeline[timeline_index].end_time < reuse_datetime:
            added_time_slot = TimeSlot(
                id=generate_uuid(),
                start_time=reuse_datetime,
                end_time=reuse_datetime
            )
            temp_timeline.append(added_time_slot)
            temp_timeline.sort(key=lambda x: x.start_time)
            temp_timeline = filter_list_time_slots(
                time_slots=temp_timeline, min_distance=MIN_DISTANCE)
            temp_timeline_index = timeline_index + 1
        elif temp_timeline[timeline_index].end_time == reuse_datetime:
            temp_timeline_index = timeline_index

        job_remaining_time = job.estimated_time
        temp_timeline = temp_timeline.copy()
        while job_remaining_time > 0:
            x = minutes_between_two_date(
                later_date=temp_timeline[temp_timeline_index + 1].start_time,
                first_date=temp_timeline[temp_timeline_index].end_time)
            if job_remaining_time < x:
                added_working_time_slot = WorkingTimeSlot(
                    id=generate_uuid(),
                    start_time=temp_timeline[temp_timeline_index].end_time,
                    end_time=temp_timeline[temp_timeline_index].end_time +
                             timedelta(minutes=job_remaining_time),
                    job=job,
                    remaining_time=0
                )
                temp_timeline.append(added_working_time_slot)
                job_finish_time = temp_timeline[temp_timeline_index].end_time + timedelta(
                    minutes=job_remaining_time)
                temp_timeline[temp_timeline_index].end_time = job_finish_time
                job_remaining_time = 0
            elif job_remaining_time == x:
                added_working_time_slot = WorkingTimeSlot(
                    id=generate_uuid(),
                    start_time=temp_timeline[temp_timeline_index].end_time,
                    end_time=temp_timeline[temp_timeline_index].end_time + timedelta(minutes=job_remaining_time),
                    job=job,
                    remaining_time=0
                )
                temp_timeline.append(added_working_time_slot)
                job_finish_time = temp_timeline[temp_timeline_index].end_time + timedelta(
                    minutes=job_remaining_time)
                job_remaining_time = 0
                temp_timeline_index = temp_timeline_index + 1
            else:
                added_working_time_slot = WorkingTimeSlot(
                    id=generate_uuid(),
                    start_time=temp_timeline[temp_timeline_index].end_time,
                    end_time=temp_timeline[temp_timeline_index].end_time +
                             timedelta(minutes=(x)),
                    job=job,
                    remaining_time=job_remaining_time - x
                )
                temp_timeline.append(added_working_time_slot)
                job_remaining_time = job_remaining_time - x
                temp_timeline_index = temp_timeline_index + 1

        if job_finish_time > job.late_finish_time:
            updated_timeline = timeline
        else:
            temp_timeline.sort(key=lambda x: x.start_time)
            updated_timeline = filter_list_time_slots(
                time_slots=temp_timeline, min_distance=MIN_DISTANCE)
            updated_start_time_reused_job.append(job)

        return updated_timeline, updated_start_time_reused_job


def set_individual_schedule(flextime_jobs: List[Job], timeline: List[TimeSlot]):
    print('set_individual_schedule')
    temp_timeline = timeline.copy()
    temp_timeline_index = 0
    added_working_time_slots = []
    for job in flextime_jobs:
        # print(job, "job in set timeline")
        job_remaining_time = job.estimated_time
        while job_remaining_time > 0:
            x = minutes_between_two_date(
                later_date=temp_timeline[temp_timeline_index + 1].start_time,
                first_date=temp_timeline[temp_timeline_index].end_time)
            if job_remaining_time < x:
                added_working_time_slot = WorkingTimeSlot(
                    id=generate_uuid(),
                    start_time=temp_timeline[temp_timeline_index].end_time,
                    end_time=temp_timeline[temp_timeline_index].end_time + timedelta(minutes=job_remaining_time),
                    job=job,
                    remaining_time=0
                )
                temp_timeline.append(added_working_time_slot)
                added_working_time_slots.append(added_working_time_slot)
                job_finish_time = temp_timeline[temp_timeline_index].end_time + timedelta(
                    minutes=job_remaining_time)
                temp_timeline[temp_timeline_index].end_time = job_finish_time
                job_remaining_time = 0
            elif job_remaining_time == x:
                added_working_time_slot = WorkingTimeSlot(
                    id=generate_uuid(),
                    start_time=temp_timeline[temp_timeline_index].end_time,
                    end_time=temp_timeline[temp_timeline_index].end_time + timedelta(minutes=job_remaining_time),
                    job=job,
                    remaining_time=0
                )
                temp_timeline.append(added_working_time_slot)
                added_working_time_slots.append(added_working_time_slot)
                job_finish_time = temp_timeline[temp_timeline_index].end_time + timedelta(minutes=job_remaining_time)
                job_remaining_time = 0
                temp_timeline_index = temp_timeline_index + 1
            else:
                added_working_time_slot = WorkingTimeSlot(
                    id=generate_uuid(),
                    start_time=temp_timeline[temp_timeline_index].end_time,
                    end_time=temp_timeline[temp_timeline_index].end_time + timedelta(minutes=x),
                    job=job,
                    remaining_time=job_remaining_time - x
                )
                temp_timeline.append(added_working_time_slot)
                added_working_time_slots.append(added_working_time_slot)
                job_remaining_time = job_remaining_time - x
                temp_timeline_index = temp_timeline_index + 1
    return temp_timeline, added_working_time_slots


class Tabu:
    best_solution: Individual
    neighbors: List[Individual]
    tabu_list: List

    def __init__(self):
        self.neighbors = []
        self.tabu_list = []

    def __on_generation__(self,
                          schedule: Schedule,
                          timeline: List[TimeSlot],
                          start_time_reused_jobs: List[Job],
                          jobs: List[Job]):
        flextime_jobs = [job for job in jobs if (job.flextime == 1 and job not in start_time_reused_jobs)]
        random.shuffle(flextime_jobs)
        self.best_solution = Individual(flextime_jobs=flextime_jobs[:],
                                        schedule=Schedule(start_time=schedule.start_time,
                                                          end_time=schedule.end_time))
        self.best_solution.schedule.time_slots = schedule.time_slots.copy()
        _, added_working_time_slots = set_individual_schedule(flextime_jobs=self.best_solution.flextime_jobs,
                                                              timeline=copy.deepcopy(timeline))
        self.best_solution.schedule.time_slots += added_working_time_slots

    @staticmethod
    def __check_item_in_tabu_list__(x, tabu_list):
        for i in tabu_list:
            if set(i) == set(x):
                return False
        return True

    def __update_best_solution__(self):
        self.neighbors.sort(key=lambda x: x.lateness)
        # if self.best_solution.lateness >= self.neighbors[0].lateness:
        print(self.neighbors[0].lateness, self.neighbors[0].flextime_jobs)
        return self.neighbors[0]
        # return self.best_solution

    def __generate_neighbors__(self):
        neighbors_flextime_jobs = []  # List[List[Job]] Mảng các công việc không cố định của các giải pháp lân cận
        for i in range(len(self.best_solution.flextime_jobs) - 1):
            temp = copy.deepcopy(self.best_solution.flextime_jobs)
            if self.__check_item_in_tabu_list__(x=[temp[i], temp[i + 1]],
                                                tabu_list=self.tabu_list):
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
                neighbors_flextime_jobs.append(temp)
                self.tabu_list.append([temp[i], temp[i + 1]])
        return neighbors_flextime_jobs


    @staticmethod
    def __fitness_func__(individual: Individual):
        flextime_jobs = individual.flextime_jobs
        schedule_lateness = 0
        working_time_slots = [w for w in individual.schedule.time_slots if isinstance(w, WorkingTimeSlot)]
        for time_slot in working_time_slots:
            for job in flextime_jobs:
                if job.id == time_slot.job.id:
                    if time_slot.start_time < job.early_start_time:
                        return LATENESS_MAX
                    if time_slot.remaining_time == 0:
                        if time_slot.end_time > job.late_finish_time:
                            job_lateness = minutes_between_two_date(time_slot.end_time, job.late_finish_time)
                        else:
                            job_lateness = 0
                        schedule_lateness += job_lateness
        return schedule_lateness

    def schedule_generation(self,
                            schedule_start_time: datetime,
                            schedule_end_time: datetime,
                            jobs: List[Job],
                            scheduled_working_time_slots: List[WorkingTimeSlot],
                            breaking_time_slots: List[BreakingTimeSlot]):
        temp_breaking_time_slots = copy.deepcopy(breaking_time_slots)
        schedule = schedule_generate(start_time=schedule_start_time,
                                     end_time=schedule_end_time)
        schedule = add_breaking_time_slots(schedule=schedule,
                                           time_slots=breaking_time_slots)
        schedule = add_fixed_time_working_time_slots(schedule=schedule,
                                                     jobs=jobs)
        timeline, start_time_reused_jobs = add_reused_working_time_slots(
            schedule=schedule,
            reused_working_time_slots=scheduled_working_time_slots,
            jobs=jobs)

        validated = validate_input_data(schedule=schedule,
                                        jobs=jobs,
                                        schedule_breaking_time_slots=temp_breaking_time_slots)
        population = []
        if validated:
            acceptable_individual = {}
            generate_success = False
            while not generate_success:
                self.__on_generation__(schedule=schedule,
                                       timeline=timeline,
                                       start_time_reused_jobs=start_time_reused_jobs,
                                       jobs=jobs)
                self.best_solution.lateness = self.__fitness_func__(self.best_solution)
                if self.best_solution.lateness == LATENESS_MAX:
                    population.append({
                        'working_time_slots': [item.serialize() for item in self.best_solution.schedule.time_slots],
                        'lateness': self.best_solution.lateness
                    })
                    generate_success = False
                else:
                    generate_success = True
            done = False
            population = []
            while not done:
                self.best_solution.lateness = self.__fitness_func__(self.best_solution)
                if self.best_solution.lateness == 0 and len(self.best_solution.schedule.time_slots) != 0:
                    acceptable_individual = self.best_solution
                    print(self.best_solution.lateness, self.best_solution.flextime_jobs)
                    population.append({
                        'working_time_slots': [item.serialize() for item in acceptable_individual.schedule.time_slots],
                        'lateness': acceptable_individual.lateness
                    })
                    done = True
                else:
                    neighbors_flextime_jobs = self.__generate_neighbors__()
                    for j in neighbors_flextime_jobs:
                        new_individual = Individual(flextime_jobs=j,
                                                    schedule=Schedule(start_time=schedule_start_time,
                                                                      end_time=schedule_end_time))
                        _, added_working_time_slots = set_individual_schedule(
                            flextime_jobs=j,
                            timeline=copy.deepcopy(timeline))
                        new_individual.schedule.time_slots += added_working_time_slots
                        new_individual.lateness = self.__fitness_func__(individual=new_individual)
                        self.neighbors.append(new_individual)
                        population.append({
                            'working_time_slots': [item.serialize() for item in new_individual.schedule.time_slots],
                            'lateness': new_individual.lateness
                        })
                    self.best_solution = self.__update_best_solution__()
            if acceptable_individual:
                output_filename = generate_uuid()+'.txt'
                output_filename = 'population'+output_filename
                with open(f'{output_filename}', 'w') as file:
                    json.dump(population, file, indent=2, separators=(',', ':'), ensure_ascii=False)
                acceptable_individual.schedule.time_slots.sort(key=lambda x: x.start_time)
                res = {
                    'result': acceptable_individual.schedule.serialize()['time_slots']
                }
            return res, len(population), output_filename

