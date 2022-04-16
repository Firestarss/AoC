import re
input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

pattern = re.compile("-?\d+")
input = [list(map(int, re.findall(pattern, x))) for x in input]
input = [[x[:2], x[2:]] for x in input]

def graph(stars, x_bounds, y_bounds):
    if x_bounds[1] - x_bounds[0] < 100:
        for i in range(y_bounds[0], y_bounds[1] + 1):
            for j in range(x_bounds[0], x_bounds[1] + 1):
                print("#" if [j,i] in stars else " ", end="")

            print()
    print()

def update(stars):
    for i in range(len(stars)):
        stars[i] = [[stars[i][0][0] + stars[i][1][0], stars[i][0][1] + stars[i][1][1]], stars[i][1]]

def part1():
    vert = -1
    last_stars = []
    last_x = []
    last_y = []

    i = 0
    while True:
        update(input)

        stars = [x[0] for x in input]
        flat_x = [x[0] for x in stars]
        flat_y = [x[1] for x in stars]
        x_bounds = (min(flat_x), max(flat_x))
        y_bounds = (min(flat_y), max(flat_y))

        temp_vert = y_bounds[1] - y_bounds[0]
        if vert == -1: vert = temp_vert

        if temp_vert > vert:
            graph(last_stars, last_x, last_y)
            print(i)
            break

        vert = temp_vert
        last_stars, last_x, last_y = [stars, x_bounds, y_bounds]

        i += 1

part1()