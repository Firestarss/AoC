import re

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = [int(x) for x in re.split("\s+",line.strip())]
        temp.sort()
        data.append(temp)

possible = 0
for point in data:
    if point[0] + point[1] > point[2]:
        possible += 1

print(possible)
