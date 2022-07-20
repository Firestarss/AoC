import copy
from threading import local
from webbrowser import get

from numpy import empty, empty_like
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    start_grid =  [list(a.strip()) for a in f.readlines()]

def get_adj(grid, pos):
    neighbors = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
    neighbors = [x for x in neighbors if 0<=x[0]+pos[0]<len(grid) and 0<=x[1]+pos[1]<len(grid[0])]
    neighbors = [(pos[0]+x[0], pos[1]+x[1]) for x in neighbors]

    return sum([grid[x[0]][x[1]] == "#" for x in neighbors])

def get_los(grid, pos):
    directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
    count = 0
    for direction in directions:
        completed = False
        cur = pos
        while 0<=cur[0]+direction[0]<len(grid) and 0<=cur[1]+direction[1]<len(grid[0]) and not completed:
            cur = (cur[0] + direction[0], cur[1] + direction[1])
            if grid[cur[0]][cur[1]] != ".": 
                completed = True
                if grid[cur[0]][cur[1]] == "#": count += 1

    return count


def solve(mode):
    updated = True
    grid = copy.deepcopy(start_grid)
    seating = {"los":get_los, "adj":get_adj}
    empty_limit = {"los":5, "adj":4}
    while updated:
        updated = False
        local_grid = copy.deepcopy(grid)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "L" and seating[mode](grid, (i, j)) == 0:
                    local_grid[i][j] = "#"
                    updated = True
                if grid[i][j] == "#" and seating[mode](grid, (i, j)) >= empty_limit[mode]:
                    local_grid[i][j] = "L"
                    updated = True
        grid = local_grid

    print(sum([x.count("#") for x in grid]))

solve("adj")
solve("los")