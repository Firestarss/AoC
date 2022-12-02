input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  ["".join(a.strip().split(" ")) for a in f.readlines()]

def part1():
    beat = {"AX":3+1, "AY":6+2, "AZ":0+3, "BX":0+1, "BY":3+2, "BZ":6+3, "CX":6+1, "CY":0+2, "CZ":3+3}
    print(sum([beat[x] for x in lines]))

def part2():
    beat = {"AX":0+3, "AY":3+1, "AZ":6+2, "BX":0+1, "BY":3+2, "BZ":6+3, "CX":0+2, "CY":3+3, "CZ":6+1}
    print(sum([beat[x] for x in lines]))

part1()
part2()