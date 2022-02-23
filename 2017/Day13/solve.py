filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input = {int(x.split(": ")[0]):int(x.split(": ")[1]) for x in input}


def part1(input):
    count = 0
    for i in input:
        if i % ((input[i] - 1) * 2) == 0:
            count += i * input[i]

    print(count)

def part2(input):
    delay = 0
    while True:
        caught = False
        delay += 1
        for i in input:
            if (delay + i) % ((input[i] - 1) * 2) == 0:
                caught = True
                break

        if not caught:
            print(delay)
            break


part1(input)
part2(input)