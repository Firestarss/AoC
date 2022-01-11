import re

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

for point in data:
    last_dash = point.rfind('-')
    first_bracket = point.rfind('[')

    point = point[:last_dash] + "*" + point[last_dash+1:first_bracket] + "*" + point[first_bracket+1:-1]
    point = point.split("*")
    point[0] = point[0].replace("-", "")
    print(point)