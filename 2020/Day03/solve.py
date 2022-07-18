import math

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [list(a.strip()) for a in f.readlines()]

def trees_hit(slope):
    right, down = slope
    height = len(lines)
    width = len(lines[0])
    pos = [0, 0]
    collisions = 0

    while pos[1] < height:
        if lines[pos[1]][pos[0] % width] == "#":
            collisions += 1

        pos = [pos[0] + right, pos[1] + down]

    return collisions

def solve():
    tests = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    hits = [trees_hit(test) for test in tests]

    print(hits[1])
    print(math.prod(hits))

solve()