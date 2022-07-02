from typing import List

from src.core.tabu_algorithm.src.common import generate_uuid
from src.core.tabu_algorithm.src.models.job import Job
from src.core.tabu_algorithm.src.models.schedule import Schedule


class Individual:
    id: str
    flextime_jobs: List[Job]
    schedule: Schedule
    lateness: float

    def __init__(self, flextime_jobs: List[Job], schedule: Schedule) -> None:
        self.id = generate_uuid()
        self.flextime_jobs = flextime_jobs
        self.schedule = schedule
