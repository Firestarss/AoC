import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def part1():
    total = 0
    for line in lines:
        l1 = re.findall(r"\d", line)
        total += int(l1[0]+l1[-1])

    print(total)
        

def part2():
    total = 0
    string_to_num = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for line in lines:
        l1 = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line.lower())
        l2 = []
        for cell in l1:
            if cell in string_to_num:
                l2.append(string_to_num[cell])
            else:
                l2.append(cell)

        total += int(l2[0]+l2[-1])

    print(total)

part1()
part2()