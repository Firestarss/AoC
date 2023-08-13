import re
import copy

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

def solve():
    max_bot = 0
    part1_complete = False
    part2_complete = False
    for line in input:
        max_bot = max(max([int(x) for x in re.findall(r"bot (\d+)", line)]), max_bot)

    bots = {key:list() for key in range(max_bot + 1)}
    outputs = {key:list() for key in range(max_bot + 1)}

    i = 0
    while True:
        cur = input[i % len(input)]
        i += 1

        if cur.startswith("value"):
            params = [int(x) for x in re.findall(r"\d+", cur)]
            if params[0] not in bots[params[1]]:
                bots[params[1]].append(params[0])

        else:
            split = cur.split(" ")
            params = [int(split[1]), split[5], int(split[6]), split[10], int(split[11])]

            if len(bots[params[0]]) != 2:
                continue
            
            low = min(bots[params[0]])
            high = max(bots[params[0]])

            if params[1] == "bot" and low not in bots[params[2]]:
                bots[params[2]].append(low)
            elif params[1] == "output" and low not in outputs[params[2]]:
                outputs[params[2]].append(low)

            if params[3] == "bot" and high not in bots[params[4]]:
                bots[params[4]].append(high)
            elif params[3] == "output" and high not in outputs[params[4]]:
                outputs[params[4]].append(high)

            if low == 17 and high == 61 and not part1_complete:
                print(params[0])
                part1_complete = True

            if outputs[0] and outputs[1] and outputs[2] and not part2_complete:
                print(outputs[0][0] * outputs[1][0] * outputs[2][0])
                part2_complete = True

            if part1_complete and part2_complete:
                break

solve()