import re

input_files = ["input.txt", "test_input.txt"]

file = 1
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

symbols = {}
gear_symbols = {}
nums = []

for (i, line) in enumerate(lines):
    for (j, c) in enumerate(line):
        if c not in "1234567890.":
            symbols[(i,j)] = c
        if c == "*":
            gear_symbols[(i,j)] = []

for (i, line) in enumerate(lines):
    iter_nums = re.finditer("\d+", line)
    for num in iter_nums:
        nums.append((int(lines[i][num.start():num.end()]), i, list(range(num.start(), num.end()))))

def part1():
    total = 0
    for num in nums:
        for adj in adj_coords([(num[1], x) for x in num[2]]):
            if adj in symbols:
                total += num[0]
                break

    print(total)

def part2():
    total = 0
    for num in nums:
        for adj in adj_coords([(num[1], x) for x in num[2]]):
            if adj in gear_symbols:
                gear_symbols[adj].append(num[0])

    for gear in gear_symbols:
        if len(gear_symbols[gear]) == 2:
            total += gear_symbols[gear][0] * gear_symbols[gear][1]

    print(total)

def adj_coords(points):
    output = set()
    adj = [(1,0), (-1,0), (0,1), (0,-1),
           (1,1), (-1,-1), (-1,1), (1,-1)]
    for point in points:
        for a in adj:
            output.add((point[0] + a[0], point[1] + a[1]))

    return output

part1()
part2()