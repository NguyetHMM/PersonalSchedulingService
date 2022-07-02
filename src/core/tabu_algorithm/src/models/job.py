from datetime import datetime

class Job:
    id: str
    name: str
    early_start_time: datetime
    late_finish_time: datetime
    start_time: datetime
    finish_time: datetime
    estimated_time: int
    flextime: bool

    def __init__(self, id, name, early_start_time, late_finish_time, start_time, finish_time, estimated_time,
                 flextime=1):
        self.id = id
        self.name = name
        self.early_start_time = early_start_time
        self.late_finish_time = late_finish_time
        self.start_time = start_time
        self.finish_time = finish_time
        self.estimated_time = estimated_time
        self.flextime = flextime

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'early_start_time': datetime.strftime(self.early_start_time, '%Y-%m-%d %H:%M:%S'),
            'late_finish_time': datetime.strftime(self.late_finish_time, '%Y-%m-%d %H:%M:%S'),
            'start_time': self.start_time,
            'finish_time': self.finish_time,
            'estimated_time': self.estimated_time,
            'flextime': self.flextime,
        }

