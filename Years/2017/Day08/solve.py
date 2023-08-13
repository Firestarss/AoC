with open("input.txt", "r") as infile:
    input = infile.read().strip().split("\n")

registers_dict = {register:0 for register in set([x.split(" ")[0] for x in input])}
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