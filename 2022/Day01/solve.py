input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.read().split("\n\n")]
    elves = sorted([sum(list(map(int, a.split('\n')))) for a in lines])[::-1]

def part1():
    print(elves[0])

def part2():
    print(sum(elves[0:3]))

part1()
part2()