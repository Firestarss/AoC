import re
from itertools import combinations_with_replacement as cwr
from itertools import permutations
input_files = ["input.txt", "test_input.txt"]

file = 1
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def apply_mask(mask, value):
    value = list(bin(value)[2:].zfill(36))

    for i in range(36):
        if mask[i] in ["1", "0"]: value[i] = mask[i]

    return(int("".join(value), 2))

def apply_mask_v2(mask, value):
    value = list(bin(value)[2:].zfill(36))

    for i in range(36):
        if mask[i] == "1": value[i] = mask[i]

    return(int("".join(value), 2))

def generate_masks(mask):
    n = mask.count("X")
    xs_set = set()
    masks = []
    for combo in cwr(["0", "1"], n):
        xs_set = xs_set.union(set(permutations(combo)))

    for xs in xs_set:
        xs = list(xs)
        masks.append("".join([xs.pop() if x == "X" else x for x in mask]))

    return(masks)


def part1():
    mask = 0
    memory = {}
    for line in lines:
        if line.startswith("mask"):
            mask = re.findall("[X01]{36}", line)[0]
        else:
            value = list(map(int, re.findall("\d+", line)))
            memory[value[0]] = apply_mask(mask, value[1])

    print(sum(memory.values()))

def part2():
    masks = []
    memory = {}
    for line in lines:
        if line.startswith("mask"):
            masks = generate_masks(re.findall("[X01]{36}", line)[0])
        else:
            value = list(map(int, re.findall("\d+", line)))
            for mask in masks:
                memory[apply_mask_v2(mask, value[0])] = value[1]

    print(sum(memory.values()))

part1()
part2()