

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

def part1():
    print(len(get_loop())//2)
            

def part2():
    loop = {k:grid[k] for k in get_loop()}
    print_grid(loop)

    inside = 0

    max_row = max([x[0] for x in grid]) + 1
    max_col = max([x[1] for x in grid]) + 1
    min_row = min([x[0] for x in grid])
    min_col = min([x[1] for x in grid])

    limits = (max_row, max_col, min_row, min_col)

    for r_i in range(min_row, max_row):
        for c_i in range(min_col, max_col):
            if is_inside((r_i, c_i), loop, limits):
                inside += 1

    print(inside)

def is_inside(coord, loop, limits):
    if coord in loop: return False
    

def print_grid(grid):
    max_row = max([x[0] for x in grid])
    max_col = max([x[1] for x in grid])
    min_row = min([x[0] for x in grid])
    min_col = min([x[1] for x in grid])

    for row_idx in range(min_row, max_row + 1):
        row = []
        for col_idx in  range(min_col, max_col + 1):
            row.append(grid[(row_idx, col_idx)] if (row_idx, col_idx) in grid else " ")
        print("".join(row))

def get_loop():
    n, s, e, w = ((-1, 0), (1, 0), (0, 1), (0, -1))
    dirs = {
        "|": [n, s],
        "-": [e, w],
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

    q = [(start)]
    v = set([start])

    while q:
        cur_coord = q.pop(0)
        cur_dir_key = grid[cur_coord]

        for dir in dirs[cur_dir_key]:
            neighbor = (cur_coord[0] + dir[0], cur_coord[1] + dir[1])

            if neighbor in grid and neighbor not in v:
                q.append(neighbor)
                v.add(neighbor)
        
    return v

part1()
part2()