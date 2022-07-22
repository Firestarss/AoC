from copy import copy
from itertools import combinations_with_replacement, permutations
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

active3 = set()
active4 = set()
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "#":
            active3.add((i,j,0))

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "#":
            active4.add((i,j,0,0))

adjs3 = set()
adjs4 = set()
for combo in combinations_with_replacement([-1, 0, 1], 3):
    if combo == (0,0,0): continue
    for perm in permutations(combo):
        adjs3.add(perm)

for combo in combinations_with_replacement([-1, 0, 1], 4):
    if combo == (0,0,0,0): continue
    for perm in permutations(combo):
        adjs4.add(perm)

def active_adj3(active, pos):
    num_active = 0
    for adj in adjs3:
        if (pos[0] + adj[0], pos[1] + adj[1], pos[2] + adj[2]) in active:
            num_active += 1

    return(num_active)

def get_3x3_cube(pos):
    output = {pos}
    for adj in adjs3:
        output.add((pos[0] + adj[0], pos[1] + adj[1], pos[2] + adj[2]))

    return output

def step3(active):
    to_add = set()
    to_del = set()
    to_test = set().union(*[get_3x3_cube(x) for x in active])

    for point in to_test:
        if point in active and active_adj3(active, point) not in [2,3]: to_del.add(point)
        if point not in active and active_adj3(active, point) == 3: to_add.add(point)

    active = active.union(to_add)
    active = active.difference(to_del)

    return active

# ==========================================================================================

def active_adj4(active, pos):
    num_active = 0
    for adj in adjs4:
        if (pos[0] + adj[0], pos[1] + adj[1], pos[2] + adj[2], pos[3] + adj[3]) in active:
            num_active += 1

    return(num_active)

def get_4x4_cube(pos):
    output = {pos}
    for adj in adjs4:
        output.add((pos[0] + adj[0], pos[1] + adj[1], pos[2] + adj[2], pos[3] + adj[3]))

    return output

def step4(active):
    to_add = set()
    to_del = set()
    to_test = set().union(*[get_4x4_cube(x) for x in active])

    for point in to_test:
        if point in active and active_adj4(active, point) not in [2,3]: to_del.add(point)
        if point not in active and active_adj4(active, point) == 3: to_add.add(point)

    active = active.union(to_add)
    active = active.difference(to_del)

    return active


def part1():
    p1_active = copy(active3)
    for _ in range(6):
        p1_active = step3(p1_active)

    print(len(p1_active))

def part2():
    p2_active = copy(active4)
    for _ in range(6):
        p2_active = step4(p2_active)

    print(len(p2_active))

part1()
part2()