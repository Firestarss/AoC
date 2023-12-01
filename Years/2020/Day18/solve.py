import re
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

class M:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return M(self.v + other.v)
    def __sub__(self, other):
        return M(self.v * other.v)
    def __pow__(self, other):
        return M(self.v + other.v)

def solve(part2 = False):
    running_sum = 0
    for line in lines:
        line = line.replace("*", "-")
        if part2: line = line.replace("+", "**")
        for num in map(str, range(10)):
            line = line.replace(num, f"M({num})")
        running_sum += eval(line).v

    print(running_sum)

solve()
solve(True)
