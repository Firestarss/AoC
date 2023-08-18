import math
import re

input = 312051

def part1(input):
    cells = {}

    step = 1
    number = 1
    coord = (0,0)

    while True:
        for j in range(2):
            for i in range(step):
                cells[number] = coord
                if j == 0:
                    coord = (coord[0] + 1, coord[1])
                else:
                    coord = (coord[0], coord[1] + 1)
                number += 1

        step += 1

        for j in range(2):
            for i in range(step):
                cells[number] = coord
                if j == 0:
                    coord = (coord[0] - 1, coord[1])
                else:
                    coord = (coord[0], coord[1] - 1)
                number += 1

        step += 1

        if number > input:
            break

    print(abs(cells[input][0]) + abs(cells[input][1]))

def part2(input):
    with open("adjacent_spiral.txt", "r") as infile:
        numbers = infile.read()

    numbers = [int(x) for x in re.findall("\d+", numbers)]

    for num in numbers:
        if num > input:
            print(num)
            break

part1(input)
part2(input)
