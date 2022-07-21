input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]
lines = [(x[0], int(x[1:])) for x in lines]

def part1():
    boat = [0, 0, 0]

    for line in lines:
        dir = line[0]
        if dir == "F":
            if boat[2] % 360 == 0: dir = "E"
            elif boat[2] % 360 == 90: dir = "N"
            elif boat[2] % 360 == 180: dir = "W"
            elif boat[2] % 360 == 270: dir = "S"
        if dir == "N": boat[1] += line[1]
        if dir == "S": boat[1] -= line[1]
        if dir == "E": boat[0] += line[1]
        if dir == "W": boat[0] -= line[1]
        if dir == "L": boat[2] += line[1]
        if dir == "R": boat[2] -= line[1]

    print(abs(boat[0]) + abs(boat[1]))

def part2():
    boat = [0, 0]
    waypoint = [10, 1]
    
    for line in lines:
        dir = line[0]
        if dir == "N": waypoint[1] += line[1]
        if dir == "S": waypoint[1] -= line[1]
        if dir == "E": waypoint[0] += line[1]
        if dir == "W": waypoint[0] -= line[1]
        if dir in ["R", "L"]:
            angle = line[1]
            if dir == "R": angle *= -1
            angle %= 360

            if angle == 90: waypoint = [-waypoint[1], waypoint[0]]
            if angle == 180: waypoint = [-waypoint[0], -waypoint[1]]
            if angle == 270: waypoint = [waypoint[1], -waypoint[0]]
        if dir == "F":
            for _ in range(line[1]):
                boat[0] += waypoint[0]
                boat[1] += waypoint[1]

    print(abs(boat[0]) + abs(boat[1]))


part1()
part2()