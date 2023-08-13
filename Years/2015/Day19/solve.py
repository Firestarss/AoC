def part1(instructions, start):
    unique_mols = set()

    for i in range(len(start) - 1):
        double = start[i:i+2]

        if double in instructions:
            for replacment in instructions[double]:
                unique_mols.add(start[:i] + replacment + start[i + 2:])

    for i in range(len(start)):
        if start[i] in instructions:
            for replacment in instructions[start[i]]:
                unique_mols.add(start[:i] + replacment + start[i + 1:])

    print(len(unique_mols))

def part2(instructions, start):
    inst_list = []

    for key in instructions:
        for replacement in instructions[key]:
            inst_list.append((key, replacement))

    count = 0
    mol = start

    while mol != "e":
        for key, repl in inst_list:
            if repl in mol:
                mol = mol.replace(repl, key, 1)
                count += 1
        
    print(count)

with open("input.txt", "r") as infile:
    lines = infile.read()

lines = lines.split("\n")

instructions = {}
start = lines[-1]

for instruction in lines[:-2]:
    instruction = instruction.strip().split(" => ")

    if instruction[0] in instructions:
        instructions[instruction[0]].append(instruction[1])
    else:
        instructions[instruction[0]] = [instruction[1]]

part1(instructions, start)
part2(instructions, start)