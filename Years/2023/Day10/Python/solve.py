
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

grid = {}
start = ()
for row in range(len(lines)):
    for col in range(len(lines[row])):
        grid[(row, col)] = lines[row][col]
        if lines[row][col] == "S":
            start = (row, col)

def get_loop(start, grid):
    n, s, w, e = ((-1, 0), (1, 0), (0, -1), (0, 1))
    dirs = {
        "|": [s, n],
        "-": [w, e],
        "L": [n, e],
        "J": [n, w],
        "7": [s, w],
        "F": [s, e],
        ".": [],
        "S": []
    }
    
    for test in [(n, "|7F"), (s, "|LJ"), (e, "-J7"), (w, "-LF")]:
        test_coord = (start[0] + test[0][0], start[1] + test[0][1])
        if test_coord in grid and grid[test_coord] in test[1]:
            dirs["S"].append(test[0])

    for key in dirs:
        dirs[key].sort()

    for key in "|-LJ7F":
        if dirs[key] == dirs["S"]:
            grid[start] = key
            break

    cur_pos = start
    loop = [start]
    v = set()

    while cur_pos != start or not v:
        pre_add_len = len(v)
        v.add(cur_pos)
        if len(v) == pre_add_len:
            break
        for dir in dirs[grid[cur_pos]]:
            next_pos = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
            if next_pos not in v:
                loop.append(next_pos)
                cur_pos = next_pos
                break

    return set(loop)

def grow_grid(grid, loop):
    output = dict()
    grown_squares = {
        "|": ".|./.|./.|.",
        "-": ".../---/...",
        "L": ".|./.L-/...",
        "J": ".|./-J./...",
        "7": ".../-7./.|.",
        "F": ".../.F-/.|.",
        ".": ".../.X./..."
    }

    for cell in grid:
        if cell in loop:
            expanded = grown_squares[grid[cell]].split("/")
        else:
            expanded = grown_squares["."].split("/")
        for i in range(3):
            for j in range(3):
                output[(cell[0] * 3 + i, cell[1] * 3 + j)] = expanded[i][j]

    return output

def part1():
    loop = get_loop(start, grid)

    print(len(loop)//2)

def part2():
    loop = get_loop(start, grid)
    big_grid = grow_grid(grid, loop)
    unknown_parity = set(coord for coord in big_grid if big_grid[coord] == "X")

    q = [(0,0)]
    v = set((0,0))
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while q:
        current = q.pop()
        for dir in dirs:
            neighbor = (current[0] + dir[0], current[1] + dir[1])
            if neighbor in v:
                continue
            v.add(neighbor)
            if neighbor in big_grid and big_grid[neighbor] in ".X":
                q.append(neighbor)
                if big_grid[neighbor] == "X":
                    unknown_parity.remove(neighbor)

    print(len(unknown_parity))


part1()
part2()