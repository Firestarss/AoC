import re

input = "197487-673251"
input = [int(x) for x in input.split("-")]

def part1(input):
    count1 = 0
    count2 = 0

    for i in range(input[0], input[1]):
        cur = str(i)
        if re.search(r"(.)\1", cur) and "".join(sorted(cur)) == cur:
            count1 += 1

            if re.search(r"(\d)(?<!(?=\1)..)\1(?!\1)", cur):
                count2 += 1

    print(count1)
    print(count2)

part1(input)