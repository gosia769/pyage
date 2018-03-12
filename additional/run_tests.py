# coding=utf-8
import os

# Parameters
emas = [True, False]
mutation_prob = [0.01, 0.05, 0.1]
mutation_func = ["random", "consecutive", "inverse"]
filename = "points.csv"

proc_base = "python -m pyage.core.bootstrap pyage.tsp.tsp_conf INFO "

# Main routine

if __name__ == "__main__":
    for e in emas:
        for pr in mutation_prob:
            for m in mutation_func:
                args = " ".join([str(e), str(pr), m, filename])
                print("Executing: " + proc_base + args + "...")
                os.system(proc_base + args)
    print("Done")
