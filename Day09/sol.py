import fileinput
from functools import reduce
from operator import mul

def get_neighbors(x, y, grid):
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vals = []
    for dx, dy in neighbors:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            vals.append((nx, ny))
    return vals

def bfs(x, y, grid, visited):
    visited.add((x, y))
    for nx, ny in set(get_neighbors(x, y, grid)) - visited:
        if grid[ny][nx] == 9:
            continue
        visited.add((nx, ny))
        visited |= bfs(nx, ny, grid, visited)
    return visited


grid = []
with open("input.txt", "r") as file:
    for line in file:
        temp = line.strip()
        grid.append([int(x) for x in list(temp)])

# Part 1
lows = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        tile = grid[y][x]
        if all(grid[ny][nx] > tile for nx,ny in get_neighbors(x, y, grid)):
            lows.append((x, y))
print(sum(grid[y][x]+1 for x,y in lows))
