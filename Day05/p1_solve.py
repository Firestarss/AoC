import re
import numpy as np

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

coords = []
for point in data:
    coord = re.split("\s+->\s+", point)
    coord = [eval("(" + x + ")") for x in coord]
    coords.append(coord)

field = np.zeros((1000,1000))

for set in coords:
    if set[0][0] == set[1][0] or set[0][1] == set[1][1]:
        if set[0][0] == set[1][0]:
            x = set[0][0]
            min_y = min(set[0][1], set[1][1])
            for i in range(abs(set[0][1] - set[1][1])+1):
                field[min_y+i][x] += 1
        
        if set[0][1] == set[1][1]:
            y = set[0][1]
            min_x = min(set[0][0], set[1][0])
            for i in range(abs(set[0][0] - set[1][0])+1):
                field[y][min_x+i] += 1

print(np.count_nonzero(field>=2))