import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def solve():
    totals = [0,0]
    for line in lines:
        colors = [max(map(int, re.findall("(\d+) " + color, line))) for color in ("red", "green", "blue")]

        if colors[0] <= 12 and colors[1] <= 13 and colors[2] <= 14:
            totals[0] += int(re.findall("Game (\d+)", line)[0])

        totals[1] += colors[0] * colors[1] * colors[2]

    print(*totals, sep="\n")

solve()