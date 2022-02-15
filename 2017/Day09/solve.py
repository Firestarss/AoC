from gc import garbage


filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

def part1(input):
    depth = 0
    total = 0
    garbage = False
    deny = False
    garbage_count = 0
    for c in input[0]:
        if deny:
            deny = False
            continue

        if c == "!":
            deny = True
            continue
        
        if garbage and c != ">":
            garbage_count += 1

        if c == "{" and not garbage:
            depth += 1
            total += depth
        elif c == "}" and not garbage:
            depth -= 1

        if c == "<":
            garbage = True

        if c == ">":
            garbage = False

    print(total)
    print(garbage_count)

part1(input)