import math

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip().split(" ") for a in f.readlines()]

class Knot:
    def __init__(self, prev = None):
        if prev is not None:
            prev.set_next(self)

        self.next = None
        self.pos = [0,0]
        self.visited = {(0,0)}
        self.directions = {
            "U": (0,1), "UR": (1,1), "R": (1,0), "UL": (-1,1),
            "D": (0,-1), "DL": (-1,-1), "L": (-1,0), "DR": (1,-1),
            "": (0,0)
        }

    def set_next(self, next): self.next = next

    def get_pos(self): return self.pos

    def get_visited(self): return self.visited

    def gen_dir(self, prev_pos):
        direction = ""
        if int(math.dist(prev_pos, self.get_pos())) <= 1: return direction

        if self.pos[1] - prev_pos[1] < 0: direction += "U"
        elif self.pos[1] - prev_pos[1] > 0: direction += "D"

        if self.pos[0] - prev_pos[0] < 0: direction += "R"
        elif self.pos[0] - prev_pos[0] > 0: direction += "L"

        return direction

    def head_move(self, direction):
        self.pos[0] += self.directions[direction][0]
        self.pos[1] += self.directions[direction][1]

        self.visited.add((self.pos[0], self.pos[1]))

        if self.next: self.next.move(self)

    def move(self, prev):
        prev_pos = prev.get_pos()
        direction = self.gen_dir(prev_pos)
        self.head_move(direction)
        

def solve():
    head = None
    tail = None
    second = None
    old = None
    for i in range(10):
        if i == 0:
            head = Knot()
            old = head
        elif i == 9:
            tail = Knot(old)
        else:
            cur = Knot(old)
            old = cur
            if i == 1: second = cur

    for line in lines:
        for _ in range(int(line[1])):
            head.head_move(line[0])

    print(len(second.get_visited()))
    print(len(tail.get_visited()))

solve()