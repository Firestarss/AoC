import math

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

data = [x.strip() for x in data[0].split(",")]
coords = [0,0]
heading = 90

for point in data:
    turn = point[0]
    distance = int(point[1:])

    if turn == "R":
        heading = (heading - 90) % 360
    if turn == "L":
        heading = (heading + 90) % 360

    if heading == 0:
        coords[0] += distance
    if heading == 90:
        coords[1] += distance
    if heading == 180:
        coords[0] -= distance
    if heading == 270:
        coords[1] -= distance

print(sum([abs(x) for x in coords]))