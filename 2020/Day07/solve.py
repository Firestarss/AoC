import re
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

bags = dict()
for line in lines:
    parent = re.match("\w+ \w+", line).group(0)
    children = re.findall("\d+ \w+ \w+", line)
    children = [(int(child[:child.find(" ")]), child[child.find(" ")+1:]) for child in children]
    bags[parent] = children

def part1():
    updated = True
    containers = {"shiny gold"}

    while updated:
        updated = False
        for bag in bags:
            for child in bags[bag]:
                if child[1] in containers and bag not in containers:
                    updated = True
                    containers.add(bag)

    print(len(containers) - 1)

def part2():
    queue = ["shiny gold"]
    count = 0
    while queue:
        cur = queue.pop(0)
        for child in bags[cur]:
            for _ in range(child[0]):
                queue.append(child[1])
                count += 1

    print(count)

part1()
part2()