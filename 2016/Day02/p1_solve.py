import numpy as np

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

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