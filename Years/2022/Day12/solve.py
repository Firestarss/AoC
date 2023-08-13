import copy
import string

class Node:
    def __init__(self, pos, value):
        self.pos = pos
        self.value = value
        self.neighbors = []
        self.parent = None

    def gen_neighbors(self, cells):
        out = []
        for n in [(1,0), (-1,0), (0,1), (0,-1)]:
            if (self.pos[0] + n[0], self.pos[1] + n[1]) in cells:
                out.append(cells[(self.pos[0] + n[0], self.pos[1] + n[1])])

        self.neighbors = out

    def __str__(self):
        return (
            f"pos: {self.pos}\nvalue: {self.value}\n"
            f"neighbors:{[[n.get_pos(), n.get_value() - self.get_value()] for n in self.neighbors]}\n"
            f"parent: {None if self.parent is None else self.parent.get_pos()}"
        )

    def set_parent(self, parent): self.parent = parent

    def get_parent(self): return self.parent

    def get_neighbors(self): return self.neighbors

    def get_value(self): return self.value

    def get_pos(self): return self.pos

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [list(a.strip()) for a in f.readlines()]

values = {}

for i in range(26):
    values[list(string.ascii_lowercase)[i]] = i

values["S"] = values["a"]
values["E"] = values["z"]

S = None
E = None

cells = {}

for i in range(len(lines)):
    for j in range(len(lines[i])):
        cells[(i,j)] = Node((i,j), values[lines[i][j]])
        if lines[i][j] == "E": E = cells[(i,j)]
        if lines[i][j] == "S": S = cells[(i,j)]

for node in cells:
    cells[node].gen_neighbors(cells)

def part1():
    v = {S.get_pos()}
    q = [S]

    while q:
        cur = q.pop(0)
        for neighbor in cur.get_neighbors():
            height_diff = neighbor.get_value() - cur.get_value()
            if neighbor.get_pos() not in v and height_diff <= 1:
                v.add(neighbor.get_pos())
                q.append(neighbor)
                neighbor.set_parent(cur)

                if neighbor.get_pos() == E.get_pos():
                    q = []
                    break

    path = [E.get_parent()]
    while path[-1].get_parent() is not None:
        path.append(path[-1].get_parent())

    print(len(path))

def part2():
    v = {E.get_pos()}
    q = [E]
    lowest = E

    while q:
        cur = q.pop(0)
        for neighbor in cur.get_neighbors():
            height_diff = neighbor.get_value() - cur.get_value()
            if neighbor.get_pos() not in v and height_diff >= -1:
                v.add(neighbor.get_pos())
                q.append(neighbor)
                neighbor.set_parent(cur)

                if neighbor.get_value() == 0:
                    lowest = neighbor
                    q = []
                    break

    E.set_parent(None)
    path = [lowest.get_parent()]
    while path[-1].get_parent() is not None:
        path.append(path[-1].get_parent())

    print(len(path))

part1()
part2()