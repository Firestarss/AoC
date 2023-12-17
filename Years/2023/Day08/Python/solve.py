import re
from math import gcd

with open("input.txt") as infile:
    lines = infile.read().strip().split("\n\n")

pattern = [c for c in lines[0]]
maps = {m[0]: (m[1], m[2]) for m in re.findall("(.+) = \((.+), (.+)\)", lines[1])}

def part1():
    e = set()
    e.add("ZZZ")
    print(get_path_length("AAA", e))

def part2():
    starts = []
    ends = set()

    for key in maps:
        if key[-1] == "A":
            starts.append(key)
        elif key[-1] == "Z":
            ends.add(key)

    paths = [get_path_length(start, ends) for start in starts]
    lcm = 1
    for path_len in paths:
        lcm = lcm*path_len//gcd(lcm, path_len)
    print(lcm)
    
def get_path_length(start, ends):
    current = start
    pattern_idx = 0

    while current not in ends:
        if pattern[pattern_idx % len(pattern)] == "L":
            current = maps[current][0]
        else:
            current = maps[current][1]

        pattern_idx += 1

    return pattern_idx

part1()
part2()