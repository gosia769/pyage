# coding=utf-8
import os
import Pyro4

from pyage.core import address
from pyage.core.agent import   generate_agents, Agent
from pyage.core.locator import Pyro4Locator
from pyage.core.migration import  NoMigration
from pyage.core.statistics import SimpleStatistics
from pyage.solutions.evolution.crossover import  AverageFloatCrossover
from pyage.solutions.evolution.evaluation import  FloatRastriginEvaluation
from pyage.solutions.evolution.initializer import  FloatInitializer
from pyage.solutions.evolution.mutation import  UniformFloatMutation
from pyage.solutions.evolution.selection import TournamentSelection

agents = generate_agents("agent", int(os.environ['AGENTS']), Agent)
step_limit = lambda: 1000

size = 1000
operators = lambda: [FloatRastriginEvaluation(), TournamentSelection(size=250, tournament_size=250),
                     AverageFloatCrossover(size=size), UniformFloatMutation(probability=0.1, radius=1)]
initializer = lambda: FloatInitializer(10, size, -10, 10)

address_provider = address.AddressProvider

migration = NoMigration
locator = Pyro4Locator

ns_hostname = lambda: os.environ['NS_HOSTNAME']
pyro_daemon = Pyro4.Daemon()
daemon = lambda: pyro_daemon
stats = SimpleStatistics