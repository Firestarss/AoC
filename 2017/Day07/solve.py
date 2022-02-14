import re
from collections import Counter

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input_d = {}
for line in input:
    key = re.match("[a-z]+", line).group(0)
    weight = int(re.search("\d+", line).group(0))
    children = line[line.index("->") + 2:].strip().split(", ") if "->" in line else []

    input_d[key] = {"w": weight, "c": children}

def rec_sum(input, node):
    if input[node]["c"] == []:
        return input[node]["w"]

    return sum([rec_sum(input, c) for c in input[node]["c"]]) + input[node]["w"]

def part1(input):
    prev = list(input.keys())[0]
    moved = True

    while moved:
        moved = False
        for key in input:
            if prev in input[key]["c"]:
                prev = key
                moved = True
    
    print(prev)
    return prev

def part2(input, node):
    while len(set(values := [rec_sum(input, c) for c in input[node]["c"]])) != 1:
        numbers = Counter(values).most_common()
        value = numbers[-1][0]

        for c in input[node]["c"]:
            if rec_sum(input, c) == value:
                node = c
        
    print(input[node]["w"] + numbers[0][0] - numbers[1][0])

node = part1(input_d)
part2(input_d, node)