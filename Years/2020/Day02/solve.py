from collections import Counter

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip().split(" ") for a in f.readlines()]

def part1():
    valid = 0
    for line in lines:
        limits = tuple(map(int, line[0].split("-")))
        letter = line[1][0]

        password = Counter(line[2])

        if min(limits) <= password[letter] <= max(limits):
            valid += 1

    print(valid)

def part2():
    valid = 0
    for line in lines:
        limits = tuple(map(int, line[0].split("-")))
        limits = tuple([x - 1 for x in limits])
        letter = line[1][0]

        letters = {line[2][min(limits)], line[2][max(limits)]}

        if len(letters) == 2 and letter in letters:
            valid += 1

    print(valid)

part1()
part2()