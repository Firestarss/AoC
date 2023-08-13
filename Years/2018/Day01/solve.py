input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

input = [int(x) for x in input]

def part1():
    print(sum(input))

def part2():
    total = 0
    seen = set()
    i = 0

    while True:
        total += input[i%len(input)]
        if total in seen:
            print(total)
            break
        else:
            seen.add(total)

        i += 1

part1()
part2()