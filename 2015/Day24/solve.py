import itertools


with open("input.txt", "r") as infile:
    lines = infile.read()

nums = [int(x) for x in lines.split("\n")]

combos = itertools.combinations(nums)

