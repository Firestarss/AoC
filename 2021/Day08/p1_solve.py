import re

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

counter = 0
for point in data:
    point = re.split("\s+",point.split("|")[1][1:])

    for seg in point:
        if len(seg) in [2,4,3,7]:
            counter +=1

print(counter)