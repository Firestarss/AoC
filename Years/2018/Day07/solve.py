import networkx as nx
input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

g = nx.DiGraph([(x.split(" ")[1], x.split(" ")[7]) for x in input])

def part1():
    print("".join(nx.lexicographical_topological_sort(g)))

def part2():
    

part1()