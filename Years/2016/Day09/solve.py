filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip()

def part1(input):
    output = ""
    i = 0
    while i < len(input):
        if input[i] != "(":
            output += input[i]
            i += 1
        else:
            closing = input[i:].index(")")
            marker = [int(x) for x in input[i + 1 : i + closing].split("x")]
            repeat = input[i + closing + 1 : i + closing + 1 + marker[0]] * marker[1]
            output += repeat

            i += closing + 1 + marker[0]

    output.replace(" ", "")
    print(len(output))

def part2(input):
    weights = [1]*len(input)
    total = 0
    i = 0

    while i < len(input):
        if input[i] != "(":
            total += weights[i]
            i += 1
        else:
            closing = input[i:].index(")")
            marker = [int(x) for x in input[i + 1 : i + closing].split("x")]

            weights[i+closing+1:i+closing+1+marker[0]] = [x*marker[1] for x in weights[i+closing+1:i+closing+1+marker[0]]]

            i += closing + 1

    print(total)


part1(input)
part2(input)