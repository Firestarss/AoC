import re
import numpy as np

input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

input = [list(map(int, re.findall(r"-?\d+", x))) for x in input]

def solve():
    field = np.zeros((1000, 1000), dtype=int)
    
    for line in input:
        field[line[1]:line[1]+line[3], line[2]:line[2]+line[4]] += 1

    print(len(np.where(field > 1)[0]))

    for line in input:
        temp = field[line[1]:line[1]+line[3], line[2]:line[2]+line[4]]
        if len(np.where(temp>1)[0]) == 0:
            print(line[0])

solve()