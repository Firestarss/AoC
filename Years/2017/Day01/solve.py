with open("input.txt", "r") as infile:
    input = [int(x) for x in infile.read().strip()]

def solve(input, step):
    total = 0

    for i in range(len(input)):
        if input[i] == input[(i+step) % len(input)]:
            total += int(input[i])

    print(total)

solve(input, 1)
solve(input, len(input) // 2)