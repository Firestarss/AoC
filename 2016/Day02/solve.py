import numpy as np

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

def part1():
    keypad = np.arange(1,10)
    keypad.resize(3,3)

    key_coord = [1,1]

    code = []

    for point in data:
        for direction in point:

            if direction == "U" and key_coord[0] != 0:
                key_coord[0] -= 1
            if direction == "D" and key_coord[0] != 2:
                key_coord[0] += 1
            if direction == "R" and key_coord[1] != 2:
                key_coord[1] += 1
            if direction == "L" and key_coord[1] != 0:
                key_coord[1] -= 1
            
        code.append(keypad[key_coord[0]][key_coord[1]])

    print("".join([str(x) for x in code]))

def part2():
    PAD = [['x', 'x', '1', 'x', 'x'],
       ['x', '2', '3', '4', 'x'],
       ['5', '6', '7', '8', '9'],
       ['x', 'A', 'B', 'C', 'x'],
       ['x', 'x', 'D', 'x', 'x'],
       ]

    cur = (0, 2)  # start at '5'
    code = ""

    INSTR = {"U": (0, -1), "D": (0, 1),
            "L": (-1, 0), "R": (1, 0),
            }

    for point in data:
        for d in point:
            new_cur = (max(0, min(cur[0] + INSTR[d][0], 4)),
                        max(0, min(cur[1] + INSTR[d][1], 4)))
            if PAD[new_cur[1]][new_cur[0]] != 'x':
                cur = new_cur

        code += str(PAD[cur[1]][cur[0]])

    print(code)

part1()
part2()