import re

with open("input.txt", "r") as infile:
    input = [int(x) for x in re.findall("\d+", infile.read())]
    
running = True
codes = {1:[20151125]}
i = 1
last = 20151125

while running:
    i += 1
    codes[i] = []

    for j in range(1,i+1):
        next = last * 252533 % 33554393
        codes[j].append(next)
        last = next

        if i > input[0] + input[1]:
            print(codes[input[1]][input[0] - 1])

            running = False
            break