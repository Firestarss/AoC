from collections import defaultdict

input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n\n")

state = input[0].split("\n")[0].split(" ")[-1][0]
iterations = int(input[0].split("\n")[1].split(" ")[-2])
pos = 0
tape = defaultdict(lambda: 0)
instructions = dict()
input = input[1:]

for rule in input:
    rule = rule.split("\n")
    temp_state = rule[0].split(" ")[-1][:-1]
    instructions[temp_state] = dict()
    rule = rule[1:]
    
    for i in range(len(rule)//4):
        cur_val = int(rule[i*4].split(" ")[-1][:-1])
        write = int(rule[i*4+1].split(" ")[-1][:-1])
        move = 1 if rule[i*4+2].split(" ")[-1][:-1] == "right" else -1
        new_state = rule[i*4+3].split(" ")[-1][:-1]

        instructions[temp_state][cur_val] = (write, move, new_state)

for i in range(iterations):
    write, move, next_state = instructions[state][tape[pos]]
    tape[pos] = write
    pos += move
    state = next_state

print(len([1 for value in tape.values() if value == 1]))