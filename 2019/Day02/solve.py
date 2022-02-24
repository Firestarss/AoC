import sys
sys.path.append('../')
from intcode import Interperator
import itertools


filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split(",")

input = [int(x) for x in input]
interperator = Interperator()
interperator.load_intcode(input)

def part1():
    interperator.set(1, 12)
    interperator.set(2, 2)
    interperator.compute()

    print(interperator.get(0))

def part2():
    target = 19690720
    pairs = itertools.permutations(range(100), 2)

    for pair in pairs:
        interperator.reset()
        interperator.set(1, pair[0])
        interperator.set(2, pair[1])
        interperator.compute()

        if interperator.get(0) == target:
            print(100 * pair[0] + pair[1])
            break

part1()
part2()