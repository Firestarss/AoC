import copy
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  f.read().split("\n\n")

insts = [a.split(" ") for a in lines[1].split("\n")]
num_stacks = len(lines[0].split("\n")[-1])
stacks = lines[0].split("\n")[:-1]
d_stacks = {i: [] for i in range(1, num_stacks // 4 + 2)}

for i in range(1, num_stacks + 1, 4):
    for j in range(len(stacks)):
        if stacks[j][i] != " ":
            d_stacks[i//4 + 1].insert(0,stacks[j][i])

def part1():
    d1_stacks = copy.deepcopy(d_stacks)
    for inst in insts:
        for _ in range(int(inst[1])):
            d1_stacks[int(inst[5])].append(d1_stacks[int(inst[3])].pop())

    for i in range(len(d1_stacks)):
        print(d1_stacks[i+1][-1], end='')
    print()

def part2():
    d1_stacks = copy.deepcopy(d_stacks)
    for inst in insts:
        d1_stacks[int(inst[5])] += d1_stacks[int(inst[3])][-int(inst[1]):]
        d1_stacks[int(inst[3])] = d1_stacks[int(inst[3])][:-int(inst[1])]

    for i in range(len(d1_stacks)):
        print(d1_stacks[i+1][-1], end='')
    print()

part1()
part2()