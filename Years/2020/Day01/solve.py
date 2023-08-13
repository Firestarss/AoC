from itertools import combinations
import math

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    data =  [int(a.strip()) for a in f.readlines()]

def sum_combos(r):
    combos = combinations(data, r)
    for combo in combos:
        if sum(combo) == 2020:
            return math.prod(combo)

print(sum_combos(2))
print(sum_combos(3))