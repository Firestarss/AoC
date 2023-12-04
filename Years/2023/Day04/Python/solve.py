import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def solve():
    copies = {i:1 for i in range(len(lines))}

    p1_total = 0

    for (i, line) in enumerate(lines):
        line = line.split(": ")[-1]
        line = line.split(" | ")

        s1 = set(re.findall(r"\d+", line[0]))
        s2 = set(re.findall(r"\d+", line[1]))

        intersection = s1.intersection(s2)
        p1_total += int(2**(len(intersection)-1))

        for j in range(len(intersection)):
            copies[i + j + 1] += copies[i]

    p2_total = sum(copies[copy] for copy in copies)

    print(p1_total)
    print(p2_total)

solve()