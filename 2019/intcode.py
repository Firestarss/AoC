# import sys
# sys.path.append('../')
# from intcode import compute

class Interperator:
    debug = False
    opcodes = {}
    intcode = []
    original_intcode = []
    index = 0

    def __init__(self):
        self.opcodes = {
        1 : (self.add, 3),
        2 : (self.multiply, 3)
        }

    def compute(self):
        if self.debug: print(f"\n>>Computing...\n")
        while self.index < len(self.intcode):
            opcode = self.intcode[self.index]
            if self.debug: print(f">>Opcode {opcode}")

            if opcode == 99:
                if self.debug: print(f">>Terminating...\n\n{self.intcode}")
                break

            action = self.opcodes[opcode][0]
            num_params = self.opcodes[opcode][1]

            action(self.intcode[self.index + 1: self.index + 1 + num_params])

    def check_changed(self):
        return not self.original_intcode == self.intcode

    def reset(self):
        self.intcode = self.original_intcode[:]
        self.index = 0
        
        if self.debug: print(f">>Reset index to {self.index} and intcode to original\n\n{self.intcode}\n\n")


    def set_debug(self, state):
        self.debug = state
        print(f">>Debug mode: {self.debug}")

    def load_intcode(self, intcode):
        self.original_intcode = intcode[:]
        self.intcode = self.original_intcode[:]

        if self.debug: print(f">>Loaded\n\n{self.intcode}\n\ninto self.intcode")

    def set(self, idx, value):
        assert type(idx) == int, "idx not an int"
        assert type(value) == int, "value not an int"
        self.intcode[idx] = value

        if self.debug: print(f">>Set index {idx} to {self.intcode[idx]}")

    def get(self, idx):
        return self.intcode[idx]

    def add(self, params):
        a1, a2, pos = params
        a1 = self.intcode[a1]
        a2 = self.intcode[a2]

        result = a1 + a2
        self.intcode[pos] = result
        self.index += 4

        if self.debug: print(f">>Inserted {a1} + {a2} = {result} into {pos}: {self.intcode[pos]== result}")

    def multiply(self, params):
        m1, m2, pos = params
        m1 = self.intcode[m1]
        m2 = self.intcode[m2]

        result = m1 * m2
        self.intcode[pos] = result
        self.index += 4

        if self.debug: print(f">>Inserted {m1} * {m2} = {result} into {pos}: {self.intcode[pos]== result}")