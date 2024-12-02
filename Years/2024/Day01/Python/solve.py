

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip().split() for a in f.readlines()]
    l1 = [int(x[0]) for x in lines]
    l2 = [int(x[1]) for x in lines]

def part1():
    l1s = sorted(l1)
    l2s = sorted(l2)
    out = [abs(l1s[i] - l2s[i]) for i in range(len(l1))]
    print(sum(out))

def part2():
    out = [x * l2.count(x) for x in l1]
    print(sum(out))

part1()
part2()