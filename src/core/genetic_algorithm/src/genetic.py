import copy
import json
import math
import random
from datetime import datetime, timedelta
from typing import List

from flask import jsonify

from src.core.genetic_algorithm.src.common import generate_uuid, MIN_DISTANCE, weekday_count, text_to_vector, \
    get_cosine, MIN_COSINE_SIMILARITY, string_to_datetime, minutes_between_two_date
from src.core.genetic_algorithm.src.models.individual import Individual
from src.core.genetic_algorithm.src.models.job import Job
from src.core.genetic_algorithm.src.models.schedule import Schedule
from src.core.genetic_algorithm.src.models.time_slot import WorkingTimeSlot, BreakingTimeSlot, TimeSlot
from src.core.genetic_algorithm.src.validate import validate_input_data

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
    for x in time_slots:
        print(type(x), x)
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
                    end_time=temp_timeline[temp_timeline_index].end_time +
                             timedelta(minutes=(job_remaining_time)),
                    job=job,
                    remaining_time=0
                )
                temp_timeline.append(added_working_time_slot)
                added_working_time_slots.append(added_working_time_slot)
                job_finish_time = temp_timeline[temp_timeline_index].end_time + timedelta(
                    minutes=(job_remaining_time))
                temp_timeline[temp_timeline_index].end_time = job_finish_time
                job_remaining_time = 0
            elif job_remaining_time == x:
                added_working_time_slot = WorkingTimeSlot(
                    id=generate_uuid(),
                    start_time=temp_timeline[temp_timeline_index].end_time,
                    end_time=temp_timeline[temp_timeline_index].end_time +
                             timedelta(minutes=(job_remaining_time)),
                    job=job,
                    remaining_time=0
                )
                temp_timeline.append(added_working_time_slot)
                added_working_time_slots.append(added_working_time_slot)
                job_finish_time = temp_timeline[temp_timeline_index].end_time + timedelta(
                    minutes=(job_remaining_time))
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
                added_working_time_slots.append(added_working_time_slot)
                job_remaining_time = job_remaining_time - x
                temp_timeline_index = temp_timeline_index + 1
    return temp_timeline, added_working_time_slots


class Genetic:

    @staticmethod
    def __on_generation__(schedule: Schedule,
                          timeline: List[TimeSlot],
                          start_time_reused_jobs: List[Job],
                          jobs: List[Job]):
        flextime_jobs = [job for job in jobs if (job.flextime == 1 and job not in start_time_reused_jobs)]
        population = []
        num_individual = 10
        for i in range(num_individual):
            # print("______________________________")
            # print("individual", i)

            random.shuffle(flextime_jobs)
            individual = Individual(flextime_jobs=flextime_jobs[:],
                                    schedule=Schedule(start_time=schedule.start_time, end_time=schedule.end_time))
            individual.schedule.time_slots = schedule.time_slots.copy()
            # individual.schedule.time_slots = set_individual_schedule(flextime_jobs=individual.flextime_jobs,
            # timeline=copy.deepcopy(timeline))
            _, added_working_time_slots = set_individual_schedule(flextime_jobs=individual.flextime_jobs,
                                                                  timeline=copy.deepcopy(timeline))
            individual.schedule.time_slots += added_working_time_slots
            population.append(individual)

            # print(end-start, "individual", i)
            # print("______________________________")
        return population

    @staticmethod
    def __on_selection__(population: List[Individual]):
        print('onselection')
        population.sort(key=lambda x: x.lateness)
        return population[:2]

    @staticmethod
    def __on_crossover__(individual1: Individual, individual2: Individual):
        print('oncrossover')
        flextime_job_ids = [i.id for i in individual1.flextime_jobs]
        parents_1 = [i.id for i in individual1.flextime_jobs]
        # print(parents_1, "parents_1")
        parents_2 = [i.id for i in individual2.flextime_jobs]
        # print(parents_2, "parents_2")

        temp_child_1_flextime_job_ids = []
        temp_child_2_flextime_job_ids = []
        child_1_flextime_job_ids = []
        child_2_flextime_job_ids = []

        # min_cross = len(flextime_job_ids)//2
        while (temp_child_1_flextime_job_ids == temp_child_2_flextime_job_ids):
            temp_child_1_flextime_job_ids = []
            temp_child_2_flextime_job_ids = []

            # x = random.randint(min_cross, (len(flextime_job_ids) - 1))
            x = len(flextime_job_ids) // 2
            crossover_gens = random.sample(parents_1, x)
            for id in parents_1:
                if id in crossover_gens:
                    temp_child_1_flextime_job_ids.append(id)
            for id in parents_2:
                if id in crossover_gens:
                    temp_child_2_flextime_job_ids.append(id)
        i = 0
        for p in parents_1:
            if p in temp_child_1_flextime_job_ids:
                child_1_flextime_job_ids.append(temp_child_2_flextime_job_ids[i])
                i += 1
            else:
                child_1_flextime_job_ids.append(p)
        j = 0
        for p in parents_2:
            if p in temp_child_2_flextime_job_ids:
                child_2_flextime_job_ids.append(temp_child_1_flextime_job_ids[j])
                j += 1
            else:
                child_2_flextime_job_ids.append(p)

        return child_1_flextime_job_ids, child_2_flextime_job_ids

    @staticmethod
    def __on_mutation__(individual: Individual):
        print('onmutation')
        new_flextime_jobs = individual.flextime_jobs
        mutation_gens = random.sample(new_flextime_jobs, 2)
        a, b = new_flextime_jobs.index(mutation_gens[0]), new_flextime_jobs.index(mutation_gens[1])
        new_flextime_jobs[b], new_flextime_jobs[a] = new_flextime_jobs[a], new_flextime_jobs[b]
        return new_flextime_jobs

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
        schedule = schedule_generate(start_time=schedule_start_time, end_time=schedule_end_time)
        schedule = add_breaking_time_slots(schedule, breaking_time_slots)
        schedule = add_fixed_time_working_time_slots(schedule, jobs)
        timeline, start_time_reused_jobs = add_reused_working_time_slots(
            schedule=schedule,
            reused_working_time_slots=scheduled_working_time_slots,
            jobs=jobs)
        acceptable_individual = {}
        generation = 0
        population = []
        validated = validate_input_data(schedule=schedule,
                                        jobs=jobs,
                                        schedule_breaking_time_slots=temp_breaking_time_slots)
        if validated:
            p = self.__on_generation__(schedule=schedule, timeline=timeline,
                                       start_time_reused_jobs=start_time_reused_jobs,
                                       jobs=jobs)
            population.append(p)
            done = False
            for individual in population[generation]:
                individual.lateness = self.__fitness_func__(individual=individual)
                # print(individual.lateness, len(individual.schedule.time_slots), "lateness")

                if individual.lateness == 0 and len(individual.schedule.time_slots) != 0:
                    acceptable_individual = individual
                    done = True

            while not done:
                # print(generation, "generation")
                new_generation = self.__on_selection__(population=population[generation])
                # print(new_generation, "new_generation")
                flextime_jobs_1 = []
                flextime_jobs_2 = []
                child_job_ids_on_crossover_1, child_job_ids_on_crossover_2 = self.__on_crossover__(new_generation[0],
                                                                                                   new_generation[1])
                for id in child_job_ids_on_crossover_1:
                    flextime_jobs_1 += [job for job in new_generation[0].flextime_jobs if job.id == id]
                for id in child_job_ids_on_crossover_2:
                    flextime_jobs_2 += [job for job in new_generation[1].flextime_jobs if job.id == id]

                child_on_crossover_1 = Individual(flextime_jobs=flextime_jobs_1,
                                                  schedule=Schedule(start_time=new_generation[0].schedule.start_time,
                                                                    end_time=new_generation[0].schedule.end_time))
                child_on_crossover_2 = Individual(flextime_jobs=flextime_jobs_2,
                                                  schedule=Schedule(start_time=new_generation[0].schedule.start_time,
                                                                    end_time=new_generation[0].schedule.end_time))
                _, added_working_time_slots_on_crossover_1 = set_individual_schedule(flextime_jobs=flextime_jobs_1,
                                                                                     timeline=copy.deepcopy(timeline))
                child_on_crossover_1.schedule.time_slots += added_working_time_slots_on_crossover_1

                _, added_working_time_slots_on_crossover_2 = set_individual_schedule(flextime_jobs=flextime_jobs_2,
                                                                                     timeline=copy.deepcopy(timeline))
                child_on_crossover_1.schedule.time_slots += added_working_time_slots_on_crossover_2

                new_generation.append(child_on_crossover_1)

                new_generation.append(child_on_crossover_2)

                flextime_jobs_mutation = self.__on_mutation__(new_generation[0])

                child_on_mutation = Individual(flextime_jobs=flextime_jobs_mutation,
                                               schedule=Schedule(start_time=new_generation[0].schedule.start_time,
                                                                 end_time=new_generation[0].schedule.end_time))
                # child_on_mutation.schedule.time_slots += set_individual_schedule(flextime_jobs=flextime_jobs_mutation, timeline=copy.deepcopy(timeline))
                _, added_working_time_slots_on_mutation = set_individual_schedule(flextime_jobs=flextime_jobs_mutation,
                                                                                  timeline=copy.deepcopy(timeline))
                child_on_mutation.schedule.time_slots += added_working_time_slots_on_mutation
                new_generation.append(child_on_mutation)
                # population.append(new_generation)

                for individual in new_generation:
                    individual.lateness = self.__fitness_func__(individual=individual)
                    # print(individual.lateness, len(individual.schedule.time_slots), "lateness")
                    if individual.lateness == 0 and len(individual.schedule.time_slots) != 0:
                        acceptable_individual = individual
                        done = True
                population.append(new_generation)
                generation += 1
        total_len = 0
        total_individual =[]
        for p in population:
            total_len += len(p)
            for indi in p:
                total_individual.append({
                    'working_time_slots': [item.serialize() for item in indi.schedule.time_slots],
                    'lateness': indi.lateness
                })

        # else:
        #     res = jsonify({
        #         'message': validated['message']
        #     })
        #     # res.status_code = 422

        if acceptable_individual:
            output_filename = generate_uuid()
            temp_output_filename = output_filename + '[population].txt'
            with open(f'src/core/genetic_algorithm/data_test/output/{temp_output_filename}', 'w') as file:
                json.dump(total_individual, file, indent=2, separators=(',', ':'), ensure_ascii=False)
            acceptable_individual.schedule.time_slots.sort(key=lambda x: x.start_time)
            res = {
                'result': acceptable_individual.schedule.serialize()['time_slots']
            }

        return res, total_len, output_filename
