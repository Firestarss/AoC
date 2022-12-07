import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    data =  [list(map(int, re.findall('\d+', a.strip()))) for a in f.readlines()]

def part1():
    lines = [[set(range(p[0], p[1] + 1)), set(range(p[2], p[3] + 1))] for p in data]
    ans = [l[0].issuperset(l[1]) or l[1].issuperset(l[0]) for l in lines]
    print(sum(ans))

def part2():
    lines = [[set(range(p[0], p[1] + 1)), set(range(p[2], p[3] + 1))] for p in data]
    ans = [bool(set(l[0]) & set(l[1])) for l in lines]
    print(sum(ans))

part1()
part2()