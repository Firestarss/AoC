import re
from itertools import combinations_with_replacement as cwr
from itertools import permutations
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def apply_mask(mask, value):
    value = list(bin(value)[2:].zfill(36))

    for i in range(36):
        if mask[i] in ["1", "0"]: value[i] = mask[i]

    return(int("".join(value), 2))

def generate_addresses(mask, address):
    n = mask.count("X")
    address = list(bin(address)[2:].zfill(36))
    xs_set = set()
    addresses = []
    for combo in cwr(["0", "1"], n):
        xs_set = xs_set.union(set(permutations(combo)))

    for xs in xs_set:
        xs = list(xs)
        temp = [xs.pop() if mask[i] == "X" else address[i] for i in range(len(address))]
        temp = ["1" if mask[i] == "1" else temp[i] for i in range(len(mask))]
        addresses.append(int("".join(temp), 2))

    return(addresses)


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
    mask = 0
    memory = {}
    for line in lines:
        if line.startswith("mask"):
            mask = re.findall("[X01]{36}", line)[0]
        else:
            value = list(map(int, re.findall("\d+", line)))
            addresses = generate_addresses(mask, value[0])
            for address in addresses:
                memory[address] = value[1]

    print(sum(memory.values()))

part1()
part2()