filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input = [x.split(",") for x in input]
wires = {0:list(), 1:list()}
directions = {"R":(1,0), "L":(-1,0), "U":(0,1), "D":(0,-1)}

for i in range(len(input)):
    cords = [0,0]
    for inst in input[i]:
        direction = inst[0]
        distance = int(inst[1:])
        for _ in range(distance):
            cords[0] += directions[direction][0]
            cords[1] += directions[direction][1]

            wires[i].append(tuple(cords))

shared = set(wires[0]).intersection(set(wires[1]))

print(min([abs(x[0]) + abs(x[1]) for x in shared]))
print(min([wires[0].index(x) + wires[1].index(x) + 2 for x in shared]))