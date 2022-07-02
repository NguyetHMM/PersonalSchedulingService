from typing import List

from src.core.tabu_algorithm.src.common import generate_uuid, minutes_between_two_date
from src.core.tabu_algorithm.src.exception.exception import TabuException, TabuMessageException
from src.core.tabu_algorithm.src.models.job import Job
from src.core.tabu_algorithm.src.models.schedule import Schedule
from src.core.tabu_algorithm.src.models.time_slot import BreakingTimeSlot, TimeSlot


def validate_input_data(schedule: Schedule, jobs: List[Job], schedule_breaking_time_slots: List[BreakingTimeSlot]):
    if schedule.end_time < schedule.start_time:
        raise TabuException(TabuMessageException.RANG_BUOC_4)

    fixed_time_job_time_slots = []
    fixed_time_jobs = [job for job in jobs if job.flextime == 0]
    for job in fixed_time_jobs:
        fixed_time_job_time_slot = TimeSlot(id=generate_uuid(), start_time=job.early_start_time,
                                            end_time=job.late_finish_time)
        fixed_time_job_time_slots.append(fixed_time_job_time_slot)

    print(schedule_breaking_time_slots)
    for t in schedule_breaking_time_slots:
        print("schedule_breaking_time_slots", t.__dict__)

    fixed_time_job_time_slots.sort(key=lambda x: x.start_time)
    schedule_breaking_time_slots.sort(key=lambda x: x.start_time)

    for jt in fixed_time_job_time_slots:
        for bt in schedule_breaking_time_slots:
            if not time_slot_unique(jt, bt):
                print("check__fixed_time_job_time_slots", jt.__dict__)
                print("check__schedule_breaking_time_slots", bt.__dict__)
                raise TabuException(TabuMessageException.RANG_BUOC_8)

    total_fixed_time = 0
    total_estimated_time = 0
    # for jt in fixed_time_job_time_slots:
    #     total_fixed_time += minutes_between_two_date(later_date = jt.end_time,first_date=jt.start_time)

    for bt in schedule_breaking_time_slots:
        total_fixed_time += minutes_between_two_date(later_date=bt.end_time, first_date=bt.start_time)

    available_time = minutes_between_two_date(later_date=schedule.end_time,
                                              first_date=schedule.start_time) - total_fixed_time

    for job in jobs:
        if job.early_start_time < schedule.start_time or job.late_finish_time > schedule.end_time:
            raise TabuException(TabuMessageException.RANG_BUOC_6)

        if job.early_start_time > job.late_finish_time:
            print('Thoi gian bat dau can < thoi gian ket thuc')
            return {
                'status': False,
                'message': 'Thoi gian bat dau can < thoi gian ket thuc'
            }
        # # print(type(job.estimated_time))
        # print(job.serialize())
        if minutes_between_two_date(later_date=job.late_finish_time,
                                    first_date=job.early_start_time) < job.estimated_time:
            raise TabuException(TabuMessageException.RANG_BUOC_5)

        total_estimated_time += job.estimated_time

    if total_estimated_time > available_time:
        raise TabuException(TabuMessageException.RANG_BUOC_7)

    return True


def time_slot_unique(time_slot_1: TimeSlot, time_slot_2: TimeSlot):
    if time_slot_1.start_time >= time_slot_2.end_time or time_slot_1.end_time <= time_slot_2.start_time:
        return True
    return False