filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input = [int(x) for x in input]

def run(input, part2):
    i = 0
    counter = 0
    while i < len(input):
        cp = input[:]
        if part2 and input[i] >= 3:
            cp[i] -= 1
        else:
            cp[i] += 1
        i += input[i]
        counter += 1
        input = cp


    print(counter)

run(input, False)
run(input, True)
