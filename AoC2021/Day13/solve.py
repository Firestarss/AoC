import re
import numpy as np
import matplotlib.pyplot as plt
import copy

input_files = ["input.txt", "test_input.txt"]

with open(input_files[0], 'r') as f:
    data =  [a.strip() for a in f.readlines()]

empty = data.index("")

dots = set([tuple(map(int,x.split(","))) for x in data[:empty]])
directions = [(x[x.index("=")-1], int(x[x.index("=")+1:]))for x in data[empty+1:]]

def reflect(dots, axis, value):
    working_dots = copy.deepcopy(dots)
    if axis == "x":
        for dot in dots:
            if dot[0] > value:
                working_dots.remove(dot)
                new_dot = (value - (dot[0]-value), dot[1])
                working_dots.add(new_dot)

    elif axis == "y":
        for dot in dots:
            if dot[1] > value:
                working_dots.remove(dot)
                new_dot = (dot[0], value - (dot[1]-value))
                working_dots.add(new_dot)

    return working_dots

def part1(dots):
    local_dots = copy.deepcopy(dots)

    local_dots = reflect(local_dots, directions[0][0], directions[0][1])

    print(len(local_dots))

def part2(dots):
    local_dots = copy.deepcopy(dots)

    for direction in directions:
        local_dots = reflect(local_dots, direction[0], direction[1])

    x_max = max([x[0] for x in local_dots]) + 1
    y_max = max([x[1] for x in local_dots]) + 1

    canvas = np.zeros((y_max, x_max))

    for dot in local_dots:
        canvas[dot[1]][dot[0]] = 1

    plt.imshow(canvas, cmap='hot')
    plt.show()


part1(dots)
part2(dots)