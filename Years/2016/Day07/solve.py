filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

def part1():
    count = 0
    for l in input:
        brackets = 0
        to_add = False
        for i in range(len(l) - 3):
            if l[i] == "[":
                brackets += 1
                continue
            if l[i] == "]":
                brackets -= 1
                continue

            if l[i] == l[i+3] and l[i+1] == l[i+2] and l[i] != l[i+1]:
                to_add = True
                if brackets:
                    to_add = False
                    break
            
        if to_add:   
            count += 1
                
    print(count)

def part2():
    count = 0
    for l in input:
        outside = set()
        inside = set()
        brackets = 0
        for i in range(len(l) - 2):
            if l[i] == "[":
                brackets += 1
                continue
            if l[i] == "]":
                brackets -= 1
                continue

            if l[i] == l[i + 2] and l[i] != l[i + 1]:
                if brackets == 0:
                    outside.add(l[i] + l[i+1] + l[i+2])
                else:
                    inside.add(l[i] + l[i+1] + l[i+2])

        for pattern in outside:
            counterpart = pattern[1] + pattern[0] + pattern[1]
            if counterpart in inside:
                count += 1
                break
                
    print(count)

part1()
part2()