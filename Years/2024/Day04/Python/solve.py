import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]
    t_lines = [''.join(col) for col in zip(*lines)]
    f_lines = [line[::-1] for line in lines]

def gen_diag(grid, length):
    output = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            temp = []
            for i in range(length):
                if (row + i) < len(grid) and (col + i) < len(grid[row]):
                    temp.append(grid[row + i][col + i])

            output.append("".join(temp))

    return output

def part1():
    count = 0
    count += sum([a.count("XMAS") for a in lines])
    count += sum([a.count("SAMX") for a in lines])

    count += sum([a.count("XMAS") for a in t_lines])
    count += sum([a.count("SAMX") for a in t_lines])

    diag = gen_diag(lines, 4)
    f_diag = gen_diag(f_lines, 4)

    count += len([x for x in diag if x in ["XMAS", "SAMX"]])
    count += len([x for x in f_diag if x in ["XMAS", "SAMX"]])

    print(count)

def part2():
    count = 0

    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == "A" and 0 < row < len(lines)-1 and 0 < col < len(lines[row])-1:
                if "".join([lines[row-1][col-1], lines[row+1][col+1]]) in ["SM", "MS"] and "".join([lines[row-1][col+1], lines[row+1][col-1]]) in ["SM", "MS"]:
                    count += 1

    print(count)

part1()
part2()

# 1886 too low