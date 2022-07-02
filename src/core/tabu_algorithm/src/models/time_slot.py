from datetime import datetime
from src.core.tabu_algorithm.src.models.job import Job

class TimeSlot:
    def __init__(self, id, start_time, end_time):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time

    def serialize(self):
        return {
            'id': self.id,
            'start_time': datetime.strftime(self.start_time, '%Y-%m-%d %H:%M:%S'),
            'end_time': datetime.strftime(self.end_time, '%Y-%m-%d %H:%M:%S'),
        }


class WorkingTimeSlot(TimeSlot):
    def __init__(self, id, start_time, end_time, job: Job, remaining_time):
        super().__init__(id, start_time, end_time)
        self.job = job
        self.remaining_time = remaining_time

    def serialize(self):
        return {
            'id': self.id,
            'start_time': datetime.strftime(self.start_time, '%Y-%m-%d %H:%M:%S'),
            'end_time': datetime.strftime(self.end_time, '%Y-%m-%d %H:%M:%S'),
            'job': self.job.serialize(),
            'remaining_time': self.remaining_time
        }


class BreakingTimeSlot(TimeSlot):
    def __init__(self, id, start_time, end_time):
        super().__init__(id, start_time, end_time)

    def serialize(self):
        return {
            'id': self.id,
            'start_time': datetime.strftime(self.start_time, '%Y-%m-%d %H:%M:%S'),
            'end_time': datetime.strftime(self.end_time, '%Y-%m-%d %H:%M:%S'),
        }