input_file = ["input.txt", "test_input.txt"]

with open(input_file[0], "r") as file:
    data = file.read().strip().split("\n")

def part1():
    horiz = 0
    depth = 0
    for point in data:
        point = point.split(" ")
        direction = point[0]
        value = int(point[1])

        if direction == "forward":
            horiz += value

        if direction == "down":
            depth += value

        if direction == "up":
            depth -= value

    return horiz*depth

def part2():
    pos = [0,0,0] # x,y,aim
    for point in data:
        direction, value = point.split(" ")

        if direction == "down":
            pos[2] += int(value)

        if direction == "up":
            pos[2] -= int(value)

        if direction == "forward":
            pos[0] += int(value)
            pos[1] += int(value) * pos[2]

    return pos[0] * pos[1]

print(part1())
print(part2())
