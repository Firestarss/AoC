with open("input.txt", "r") as infile:
    input = infile.read().strip().split("\n")[0].split(",")

def solve(input):
    x = y = largest = 0
    dirs = {"n":(0,2), "s":(0,-2), "ne":(1,1), "nw":(-1,1), "se":(1,-1), "sw":(-1,-1)}

    for dir in input:
        x += dirs[dir][0]
        y += dirs[dir][1]

        largest = max(abs(x) + abs(y), largest)

    print((abs(x) + abs(y))//2)
    print(largest//2)

solve(input)