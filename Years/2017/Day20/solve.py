import re
from copy import deepcopy

input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

input = [list(map(int, re.findall("-?\d+", x))) for x in input]
input = [[x[:3], x[3:6], x[6:]] for x in input]

def man_dist(l_values):
    total = 0
    for value in l_values:
        total += abs(value)

    return total

def remove_dupes(particles):
    temp_dict = {}

    for particle in particles:
        pos = tuple(particle[0])
        if pos in temp_dict:
            temp_dict[pos] += 1
        else:
            temp_dict[pos] = 1

    return [p for p in particles if temp_dict[tuple(p[0])] == 1]

def part1():
    print(input.index(sorted(input, key = lambda x: (man_dist(x[2]), man_dist(x[1]), man_dist(x[0])))[0]))


def part2():
    particles = deepcopy(input)
    for k in range(1000):
        particles = remove_dupes(particles)

        for particle in particles:
            for i in range(3):
                particle[1][i] += particle[2][i]
                particle[0][i] += particle[1][i]

    print(len(particles))

part1()
part2()