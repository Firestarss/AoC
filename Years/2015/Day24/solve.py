import itertools

from numpy import prod


with open("input.txt", "r") as infile:
    lines = infile.read()

nums = [int(x) for x in lines.split("\n")]

def balance(nums, n):
    weight = sum(nums) // n
    running = True

    for i in range(len(nums)):
        if running:
            for group1 in itertools.combinations(nums, i):
                if sum(group1) == weight:
                    product = 1
                    for x in group1:
                        product *= x
                    running = False
                    break

    print(product)


balance(nums, 3)
balance(nums, 4)