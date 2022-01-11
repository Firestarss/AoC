import copy
import numpy as np
from numpy.core.fromnumeric import searchsorted

input_files = ["input.txt", "test_input.txt", "test_input2.txt"]
data = []
with open(input_files[0], 'r') as f:
    for line in f:
        data.append(line.strip())

def step_horiz(data):
    new_data = []

    for i in range(len(data)):
        new_line = ["." for _ in range(len(data[i]))]
        for j in range(len(data[i])):
            next_spot = (j+1) % len(data[i])
            if data[i][j] == ">" and data[i][next_spot] == ".":
                new_line[next_spot] = ">"
            else:
                if new_line[j] == ".":
                    new_line[j] = data[i][j]

        new_data.append("".join(new_line))

    return new_data

def step_vert(data):
    new_data = [["." for x in range(len(data[0]))] for _ in data]

    for i in range(len(data)):
        for j in range(len(data[i])):
            next_spot = (i+1) % len(data)
            if data[i][j] == "v" and data[next_spot][j] == ".":
                new_data[next_spot][j] = "v"

            else:
                if new_data[i][j] == ".":
                    new_data[i][j] = data[i][j]

    new_data = ["".join(x) for x in new_data]
    return new_data

def step(data):
    data = step_horiz(data)
    data = step_vert(data)
    return data


def part1(data):
    counter = 0
    while True:
        counter += 1
        new_data = step(data)
        if new_data == data:
            print(counter)
            break

        data = new_data


part1(data)