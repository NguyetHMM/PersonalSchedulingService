from src.controllers.scheduling_generate_controller import GeneticSchedulingGenerate
from src.controllers.scheduling_generate_controller import TabuSchedulingGenerate


def initialize_routes(api):
    api.add_resource(GeneticSchedulingGenerate, '/genetic-scheduling')
    api.add_resource(TabuSchedulingGenerate, '/tabu-scheduling')


