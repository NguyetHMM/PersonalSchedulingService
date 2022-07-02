from datetime import datetime
from typing import List

from src.core.tabu_algorithm.src.common import generate_uuid
from src.core.tabu_algorithm.src.models.time_slot import TimeSlot


class Schedule:
    id: str
    time_slots: List[TimeSlot]
    lateness: float
    start_time: datetime
    end_time: datetime

    def __init__(self, start_time, end_time):
        self.id = generate_uuid()
        self.start_time = start_time
        self.end_time = end_time
        self.time_slots = []
        # time_slot_id = generate_uuid()
        # free_time_slot = FreeTimeSlot(id = time_slot_id, start_time = start_time, end_time= end_time)
        # self.time_slots.append(free_time_slot)

    def serialize(self):
        # for item in self.time_slots:
        #     print(type(item), item)
        # # print(self.time_slots[10].serialize())
        return {
            'id': self.id,
            'start_time': datetime.strftime(self.start_time, '%Y-%m-%d %H:%M:%S'),
            'end_time': datetime.strftime(self.end_time, '%Y-%m-%d %H:%M:%S'),
            'time_slots': [t.serialize() for t in self.time_slots],
            # 'lateness': self.lateness
        }
