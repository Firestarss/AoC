import string

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    instructions = infile.read().strip().split("\n")

class program:

    def __init__(self, program_name = 0, part = 1):
        self.p1_flag = False
        self.part = part
        self.inputs = list()
        self.registers = {key:0 for key in string.ascii_lowercase}
        self.i = 0
        self.rcv_idx = 0
        self.partner = 0
        self.program_name = program_name
        self.registers["p"] = program_name

    def step(self):
        if self.is_halted():
            return

        cur = instructions[self.i]

        if cur.startswith("snd"):
            self.partner.inputs.append(self.get_register(self.registers, cur.split(" ")[-1]))
        
        elif cur.startswith("set"):
            params = cur.split(" ")
            self.registers[params[1]] = self.get_register(self.registers, params[2])

        elif cur.startswith("add"):
            params = cur.split(" ")
            self.registers[params[1]] += self.get_register(self.registers, params[2])

        elif cur.startswith("mul"):
            params = cur.split(" ")
            self.registers[params[1]] *= self.get_register(self.registers, params[2])

        elif cur.startswith("mod"):
            params = cur.split(" ")
            self.registers[params[1]] %= self.get_register(self.registers, params[2])

        elif self.part == 1 and cur.startswith("rcv"):
            params = cur.split(" ")
            if self.get_register(self.registers, params[1]) != 0:
                self.p1_flag = True 

        elif self.part == 2 and cur.startswith("rcv"):
            params = cur.split(" ")
            if len(self.inputs) > self.rcv_idx:
                self.registers[params[1]] = self.inputs[self.rcv_idx]
                self.rcv_idx += 1  


        elif cur.startswith("jgz"):
            params = cur.split(" ")
            if self.get_register(self.registers, params[1]) > 0:
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
        if instructions[self.i].startswith("rcv") and self.rcv_idx >= len(self.inputs) - 1:
            return True
        return False

def part1():
    p1 = program()
    p1.partner = p1

    while True:
        p1.step()
        if p1.p1_flag:
            print(p1.inputs[-1])
            break

def part2():
    p0 = program(0, part = 2)
    p1 = program(1, part = 2)

    p0.partner = p1
    p1.partner = p0

    while not p0.is_halted() or not p1.is_halted():
        p0.step()
        p1.step()
        

    print(len(p0.inputs))

part1()
part2()