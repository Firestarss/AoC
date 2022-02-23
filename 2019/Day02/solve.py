import sys
sys.path.append('../')
from intcode import compute
import itertools


filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split(",")

input = [int(x) for x in input]

def part1(input):
    input_copy = input[:]
    input_copy[1] = 12
    input_copy[2] = 2

    print(compute(input_copy)[0])

def part2(input):
    target = 19690720
    pairs = itertools.permutations(range(100), 2)

    for pair in pairs:
        temp = input[:]
        temp[1] = pair[0]
        temp[2] = pair[1]

        if compute(temp)[0] == target:
            print(100 * pair[0] + pair[1])
            break

part1(input)
part2(input)