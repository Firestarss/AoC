input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    groups =  [a.strip() for a in f.read().split("\n\n")]

def part1():
    answers = [len(set(x.replace("\n", ""))) for x in groups]
    print(sum(answers))

def part2():
    answers = []
    for group in groups:
        people = group.split("\n")
        people = [set(x) for x in people]
        answers.append(len(set.intersection(*people)))

    print(sum(answers))

part1()
part2()