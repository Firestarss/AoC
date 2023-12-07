import re
import math

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

times = list(map(int, re.findall("\d+", lines[0])))
distances = list(map(int, re.findall("\d+", lines[1])))

def record_races(time, distance):
    num_beat = 0
    for j in range(time):
        temp_dist = j * (time - j)
        if temp_dist > distance:
            num_beat += 1

    return num_beat


def part1():
    print(math.prod([record_races(times[i], distances[i]) for i in range(len(times))]))


def part2():
    print(record_races(int("".join([str(x) for x in times])), int("".join([str(x) for x in distances]))))

part1()
part2()