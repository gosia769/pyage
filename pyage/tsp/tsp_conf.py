import logging

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.elect.el_init import root_agents_factory
from pyage.elect.naming_service import NamingService
from pyage.tsp.argumentParser import get_arguments
from pyage.tsp.tsp_crossover import TSPCrossover
from pyage.tsp.tsp_eval import TSPEvaluator
from pyage.tsp.tsp_init import EmasInitializer

logger = logging.getLogger(__name__)

arguments = get_arguments()

agents_count = 10
stop_condition = lambda: StepLimitStopCondition(1000)

if arguments.emas:
    logger.debug("EMAS, %s agents", agents_count)
    agents = root_agents_factory(agents_count, AggregateAgent)

    agg_size = 40
    aggregated_agents = EmasInitializer(arguments.filename, size=agg_size,
                                        energy=40)

    emas = EmasService

    minimal_energy = lambda: 10
    reproduction_minimum = lambda: 100
    migration_minimum = lambda: 120
    newborn_energy = lambda: 100
    transferred_energy = lambda: 40

    budget = 0
    evaluation = lambda: TSPEvaluator()
    crossover = lambda: TSPCrossover(size=30)
    mutation = lambda: arguments.mutation


    def simple_cost_func(x):
        return abs(x) * 10

else:
    agents = generate_agents("agent", agents_count, Agent)
    logger.debug("Not EMAS, %s agents", agents_count)

# TODO:



address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('fitness_%s_pyage.txt' % __name__)

naming_service = lambda: NamingService(starting_number=2)
