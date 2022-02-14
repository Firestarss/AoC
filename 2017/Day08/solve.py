import re

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

registers = set([re.match("^[^ ]+", x).group(0) for x in input])
registers_dict = {}

for register in registers:
    registers_dict[register] = 0

instructions = [x.split(" ") for x in input]

def solve(instructions, registers_dict):
    largest = 0
    for instruction in instructions:
        condition = "registers_dict[\"" + instruction[-3] + "\"]" + "".join(instruction[-2:])
        if eval(condition):
            if instruction[1] == "inc":
                registers_dict[instruction[0]] += int(instruction[2])
            elif instruction[1] == "dec":
                registers_dict[instruction[0]] -= int(instruction[2])

        largest = max(largest, max(registers_dict.values()))

    print(max(registers_dict.values()))
    print(largest)

solve(instructions, registers_dict)