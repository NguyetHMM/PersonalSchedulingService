import copy
import json
import time
from typing import List

from src.core.genetic_algorithm.src.common import string_to_datetime
from src.core.genetic_algorithm.src.genetic import Genetic
from src.core.genetic_algorithm.src.models.job import Job
from src.core.genetic_algorithm.src.models.time_slot import WorkingTimeSlot, BreakingTimeSlot
from src.core.tabu_algorithm.src.tabu import Tabu


class SchedulingGenerateService:
    def genetic_scheduling_generate(self,
                                    schedule_start_time,
                                    schedule_end_time,
                                    jobs,
                                    scheduled_working_time_slots,
                                    breaking_time_slots):
        run_time_start = time.time()
        start_time = string_to_datetime(schedule_start_time)
        end_time = string_to_datetime(schedule_end_time)
        schedule_breaking_time_slots = []
        schedule_jobs = []
        recent_working_time_slots: List[WorkingTimeSlot] = []
        print(breaking_time_slots)
        for bt in breaking_time_slots:
            b = BreakingTimeSlot(id=bt['id'], start_time=string_to_datetime(bt['start_time']),
                                 end_time=string_to_datetime(bt['end_time']))
            schedule_breaking_time_slots.append(b)
        temp = copy.deepcopy(schedule_breaking_time_slots)
        print(temp)
        for i in range(len(temp)):
            print("temp", temp[i].__dict__)
        for job in jobs:
            j = Job(id=job['id'],
                    name=job['name'],
                    early_start_time=string_to_datetime(job['early_start_time']),
                    late_finish_time=string_to_datetime(job['late_finish_time']),
                    start_time=None,
                    finish_time=None,
                    estimated_time=job['estimated_time'],
                    flextime=job['flextime'])
            schedule_jobs.append(j)

        for t in scheduled_working_time_slots:
            t = WorkingTimeSlot(id=t['id'],
                                start_time=string_to_datetime(t['start_time']),
                                end_time=string_to_datetime(t['end_time']),
                                job=Job(id=t['job']['id'],
                                        name=t['job']['name'],
                                        early_start_time=string_to_datetime(t['job']['early_start_time']),
                                        late_finish_time=string_to_datetime(t['job']['late_finish_time']),
                                        start_time=None,
                                        finish_time=None,
                                        estimated_time=t['job']['estimated_time'],
                                        flextime=t['job']['flextime']),
                                remaining_time=t['remaining_time'])
            recent_working_time_slots.append(t)

        genetic = Genetic()
        res, population_size, output_filename = genetic.schedule_generation(schedule_start_time=start_time,
                                                                            schedule_end_time=end_time,
                                                                            jobs=schedule_jobs,
                                                                            scheduled_working_time_slots=recent_working_time_slots,
                                                                            breaking_time_slots=temp)
        run_time_end = time.time()

        log = {
            'population_size': population_size,
            'runtime': run_time_end - run_time_start,
            'jobs_num': len(jobs),
            'accept_individual': res,

        }
        temp_output_filename = output_filename + '[result].txt'
        with open(f'src/core/genetic_algorithm/data_test/output/{temp_output_filename}', 'w') as file:
            json.dump(log, file, indent=2, separators=(',', ':'), ensure_ascii=False)

        return res
