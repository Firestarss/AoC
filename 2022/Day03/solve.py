import string

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def part1():
    data = [set.intersection(set(a[:len(a)//2]), set(a[len(a)//2:])) for a in lines]
    print(sum([(string.ascii_letters.index(list(point)[0])+1) for point in data]))

def part2():
    data = [set.intersection(set(lines[i]), set(lines[i+1]), set(lines[i+2])) for i in range(0, len(lines), 3)]
    print(sum([(string.ascii_letters.index(list(point)[0])+1) for point in data]))

part1()
part2()