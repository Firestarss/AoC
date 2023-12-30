

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

input_grid = {}
for row in range(len(lines)):
    for col in range(len(lines[row])):
        input_grid[(row,col)] = lines[row][col]

def move_rocks(grid, dir = "u"):
    rocks = {
        "u": sorted([coord for coord in grid if grid[coord] == "O"], key=lambda x: x[0]),
        "d": sorted([coord for coord in grid if grid[coord] == "O"], key=lambda x: x[0], reverse=True),
        "l": sorted([coord for coord in grid if grid[coord] == "O"], key=lambda x: x[1]),
        "r": sorted([coord for coord in grid if grid[coord] == "O"], key=lambda x: x[1], reverse=True)
    }

    dirs = {
        "u": (-1, 0),
        "d": (1, 0),
        "l": (0, -1),
        "r": (0, 1)
    }

    rocks = rocks[dir]
    
    for rock in rocks:
        grid[rock] = "."
        cur_coord = rock
        while cur_coord in grid and grid[cur_coord] == ".":
            cur_coord = (cur_coord[0] + dirs[dir][0], cur_coord[1] + dirs[dir][1])

        grid[(cur_coord[0] - dirs[dir][0], cur_coord[1] - dirs[dir][1])] = "O"

    return grid


def calculate_weight(grid):
    bottom_edge = max([x[0] for x in grid]) + 1
    rocks = [coord for coord in grid if grid[coord] == "O"]

    output = sum([abs(rock[0] - bottom_edge) for rock in rocks])
    return output

def spin(grid):
    grid = move_rocks(grid, "u")
    grid = move_rocks(grid, "l")
    grid = move_rocks(grid, "d")
    grid = move_rocks(grid, "r")

    return grid

def get_state(grid):
    return tuple(sorted([coord for coord in grid if grid[coord] == "O"]))

def part1():
    grid = {key:value for key, value in input_grid.items()}
    grid = move_rocks(grid)

    print(calculate_weight(grid))

def part2():
    grid = {key:value for key, value in input_grid.items()}
    states = dict()

    for i in range(1, 1000000000):
        grid = spin(grid)
        current_state = get_state(grid)
        if current_state in states:
            states[current_state][0].append(i)
            if len(states[current_state][0]) == 3:
                break
        else:
            states[current_state] = [[i], calculate_weight(grid)]

    for state in states:
        if len(states[state][0]) == 1:
            continue

        if (1000000000 - states[state][0][0]) % (states[state][0][1] - states[state][0][0]) == 0:
            print(states[state][1])
    

part1()
part2()