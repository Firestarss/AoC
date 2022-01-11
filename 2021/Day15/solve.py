import networkx as nx
import re
import numpy as np
import matplotlib.pyplot as plt

input_files = ["input.txt", "test_input.txt"]

with open(input_files[0], 'r') as f:
    data =  [a.strip() for a in f.readlines()]

grid = np.array([re.findall("\d", x) for x in data], dtype=int)

def gen_graph(grid):
    G = nx.DiGraph()
    adjs = [(0,1),(0,-1),(1,0),(-1,0)]

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            for adj in adjs:
                if 0 <= i + adj[0] < grid.shape[0] and 0 <= j + adj[1] < grid.shape[1]:
                    G.add_edge((i + adj[0], j + adj[1]), (i, j), w=grid[i][j])

    return G

def tile(grid):
    grid = np.hstack((grid, grid+1, grid+2, grid+3, grid+4))
    grid = np.vstack((grid, grid+1, grid+2, grid+3, grid+4))
    grid[grid > 9] += 1
    grid = grid % 10
    return grid


def part1(grid):
    G = gen_graph(grid)
    print(nx.shortest_path_length(G,(0,0),(grid.shape[0]-1,grid.shape[1]-1), "w"))

def part2(grid):
    grid = tile(grid)
    part1(grid)


part1(grid)
part2(grid)