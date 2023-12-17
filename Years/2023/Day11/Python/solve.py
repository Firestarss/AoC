from copy import copy
from itertools import combinations

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

empty_rows = set([i for i in range(len(lines))])
empty_cols = set([i for i in range(len(lines[0]))])
pois = set()

for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == "#":
            if row in empty_rows: empty_rows.remove(row)
            if col in empty_cols: empty_cols.remove(col)
            pois.add((row, col))

def solve():
    p1_pois = shift_pois(2)
    print(sum([manhattan_dist(*pair) for pair in combinations(p1_pois, 2)]))

    p2_pois = shift_pois(1000000)
    print(sum([manhattan_dist(*pair) for pair in combinations(p2_pois, 2)]))

def shift_pois(padding):
    new_pois = set()
    for cur_poi in pois:
        new_row, new_col = cur_poi
        
        for row in empty_rows:
            if row < cur_poi[0]:
                new_row += padding - 1
        
        for col in empty_cols:
            if col < cur_poi[1]:
                new_col += padding - 1

        new_pois.add((new_row, new_col))
    
    return new_pois

def manhattan_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

solve()