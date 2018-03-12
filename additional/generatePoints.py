
import argparse
import random

parser = argparse.ArgumentParser(description=("Points Generator"))
parser.add_argument('--points', '-p', type=int, dest='points', default=30,
                    help="Set the number of points to be generated")

arguments = parser.parse_args()

with open("points.csv", "w") as points:
    points.write("Id,X,Y\n")
    for i in range(arguments.points):
        points.write("{}, {}, {}\n".format(i, random.randint(1, 1000), random.randint(1, 1000)))
    points.close()
