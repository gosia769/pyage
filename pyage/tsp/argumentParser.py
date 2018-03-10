import sys

import logging

from pyage.tsp.tsp_mutation import TSPRandomMutation, TSPConsecutiveMutation

logger = logging.getLogger(__name__)


def get_arguments():
    args = sys.argv

    if len(args) < 8:
        raise ValueError("Not enough parameters!")

    return Arguments(args[3] == 'True', float(args[4]), args[5], args[6],
                     int(args[7]))


class Arguments:
    def __init__(self, emas, probability, mutation, filename, agents_count):
        self.agents_count = agents_count
        self.filename = filename
        self.probability = probability
        self.mutation = TSPRandomMutation(self.probability)\
            if mutation == "random"\
            else TSPConsecutiveMutation(self.probability)
        self.emas = emas
        self.logParameters()

    def logParameters(self):
        logger.info("Emas: " + str(self.emas))
        logger.info("Mutation: " + str(self.mutation))
        logger.info("Probability: " + str(self.probability))
        logger.info("Filename: " + str(self.filename))
        logger.info("Agents: " + str(self.agents_count))
