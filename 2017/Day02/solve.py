with open("input.txt", "r") as infile:
    input = infile.read().strip().split("\n")

input = [x.split("\t") for x in input]

for i in range(len(input)):
    for j in range(len(input[i])):
        input[i][j] = int(input[i][j])

def part1(input):
    print(sum([max(line) - min(line) for line in input]))

def part2(input):
    total = 0
    
    for line in input:
        for i in range(len(line)):
            for j in range(i + 1, len(line)):

                if line[i] % line[j] == 0:
                    total += line[i] // line[j]

                elif line[j] % line[i] == 0:
                    total += line[j] // line[i]

    print(total)

part1(input)
part2(input)