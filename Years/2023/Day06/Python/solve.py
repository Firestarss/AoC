import re
import math
with open("input.txt") as file:
    lines = file.readlines()

times = list(map(int, re.findall("\d+", lines[0])))
distances = list(map(int, re.findall("\d+", lines[1])))

def part1():
    print(math.prod([record_races(times[i], distances[i]) for i in range(len(times))]))


def part2():
    print(record_races(int("".join([str(x) for x in times])), int("".join([str(x) for x in distances]))))

def record_races(time, distance):
    num_beat = 0
    for j in range(time):
        temp_dist = j * (time - j)
        if temp_dist > distance:
            num_beat += 1

    return num_beat

part1()
part2()