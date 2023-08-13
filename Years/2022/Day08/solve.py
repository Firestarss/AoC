input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [list(map(int, list(a.strip()))) for a in f.readlines()]

def part1():
    total = 0
    for row in range(1, len(lines) - 1):
        for col in range(1, len(lines[row]) - 1):
            total += is_visible(row, col)

    print(total + (len(lines) * 2 + len(lines[0]) * 2) - 4)

def part2():
    out = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            out = max(out, score(row, col))

    print(out)


def is_visible(row, col):
    height = lines [row][col]

    left = max(lines[row][:col]) < height
    right = max(lines[row][col + 1:]) < height

    vert = [lines[x][col] for x in range(len(lines))]
    
    up = max(vert[:row]) < height
    down = max(vert[row+1:]) < height

    return left or right or up or down

def score(row, col):
    height = lines [row][col]
    
    left = lines[row][:col][::-1]
    right = lines[row][col + 1:]

    vert = [lines[x][col] for x in range(len(lines))]
    
    up = vert[:row][::-1]
    down = vert[row+1:]

    left_v = 0
    right_v = 0
    up_v = 0
    down_v = 0

    for i in range(len(left)):
        left_v += 1
        if left[i] >= height: break

    for i in range(len(right)):
        right_v += 1
        if right[i] >= height: break

    for i in range(len(up)):
        up_v += 1
        if up[i] >= height: break

    for i in range(len(down)):
        down_v += 1
        if down[i] >= height: break

    return left_v * right_v * up_v * down_v

part1()
part2()