

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        data.append(line.strip())


horiz = 0
depth = 0
aim = 0
for point in data:
    point = point.split(" ")
    direction = point[0]
    value = int(point[1])

    if direction == "forward":
        horiz += value
        depth += value * aim

    if direction == "down":
        aim += value

    if direction == "up":
        aim -= value

print("Horiz: %d\nDepth: %d\nMultiplied: %d" %(horiz, depth, horiz*depth))