import numpy as np
import re
import time

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

def solve():
    grid = np.zeros((6,50), dtype=int)

    for line in input:
        params = [int(x) for x in re.findall(r"\d+", line)]
        if line.startswith("rect"):
            grid[0:params[1], 0:params[0]] = 1

        elif line.startswith("rotate row"):
            grid[params[0]] = np.roll(grid[params[0]], params[1])

        elif line.startswith("rotate col"):
            grid = np.rot90(grid, -1)
            grid[params[0]] = np.roll(grid[params[0]], -params[1])
            grid = np.rot90(grid, 1)
        

    print(sum([sum(x) for x in grid]))

    for r in grid:
        print("".join([str(x) for x in r]).replace("1","#").replace("0", " "))

solve()