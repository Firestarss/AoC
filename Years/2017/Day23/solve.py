import string

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    instructions = infile.read().strip().split("\n")

class program:

    def __init__(self):
        self.inputs = list()
        self.registers = {key:0 for key in string.ascii_lowercase}
        self.i = 0
        self.mul_idx = 0

    def step(self):
        if self.is_halted():
            return

        cur = instructions[self.i]
        
        if cur.startswith("set"):
            params = cur.split(" ")
            self.registers[params[1]] = self.get_register(self.registers, params[2])

        elif cur.startswith("sub"):
            params = cur.split(" ")
            self.registers[params[1]] -= self.get_register(self.registers, params[2])

        elif cur.startswith("mul"):
            self.mul_idx += 1
            params = cur.split(" ")
            self.registers[params[1]] *= self.get_register(self.registers, params[2])

        elif cur.startswith("jnz"):
            params = cur.split(" ")
            if self.get_register(self.registers, params[1]) != 0:
                self.i += self.get_register(self.registers, params[2]) - 1

        self.i += 1

    def get_register(self, registers, value):
        if value in string.ascii_lowercase:
            return registers[value]
        else:
            return int(value)

    def is_halted(self):
        if self.i >= len(instructions):
            return True
        return False

def part1():
    p1 = program()
    
    while True:
        p1.step()
        if p1.is_halted():
            print(p1.mul_idx)
            break

def part2():
    a=b=c=d=e=f=g=h=0
    a=1

    b=c=81*100+100000
    c += 17000

    for i in range(b, c+1, 17):
        for j in range(2, i):
            if i % j == 0:
                h += 1
                break

    print(h)

part1()
part2()
