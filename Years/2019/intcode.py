# import sys
# sys.path.append('../')
# from intcode import Interperator

class Interperator:
    original_intcode = []
    debug = False
    opcodes = {}

    def __init__(self, debug = False):
        self.opcodes = {
        1 : (self.add, 3),
        2 : (self.multiply, 3),
        3 : (self.input, 1),
        4 : (self.output, 1)
        }

        self.debug = debug

        self.reset()

    def reset(self):
        self.intcode = self.original_intcode[:]
        self.index = 0
        self.inputs = []
        self.outputs = []
        self.param_modes = []
        
        if self.debug: print(f">>Reset")


    def compute(self):
        if self.debug: print(f"\n>>Computing...\n")
        while self.index < len(self.intcode):
            opcode = self.parse_opcode_and_params(self.intcode[self.index])
            if self.debug: print(f">>Opcode {opcode}")

            if opcode == 99:
                if self.debug: print(f">>Terminating...\n\n{self.intcode}\n\n")
                break

            action = self.opcodes[opcode][0]
            num_params = self.opcodes[opcode][1]

            action(self.intcode[self.index + 1: self.index + 1 + num_params])

    def parse_opcode_and_params(self, value):
        padded = str(value).zfill(6)
        opcode = int(padded[-2:])
        self.param_modes = [int(x) for x in padded[:-2]]

        if self.debug: print(f">>Parsing: Opcode {opcode}, param_modes: {self.param_modes}")

        return opcode

    def find_param(self, param):
        mode = self.param_modes.pop()
        if mode == 0: # Address Mode
            if self.debug: print(f">>Param Mode: 0, {param}")
            return self.intcode[param]
        if mode == 1: # Immediate Mode
            if self.debug: print(f">>Param Mode: 1, {param}")
            return param

    def add_input(self, value):
        self.inputs.append(value)

        if self.debug: print(f">>Added {value} to input list: {self.inputs}")

    def get_outputs(self):
        return self.outputs

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

    # ==============================================================================
    # ============================== OPCODE FUNCTIONS ==============================
    # ==============================================================================
    def add(self, params):
        a1, a2, idx = params
        a1 = self.find_param(a1)
        a2 = self.find_param(a2)
        idx = self.find_param(idx)

        result = a1 + a2
        self.intcode[idx] = result
        self.index += 4

        if self.debug: print(f">>Inserted {a1} + {a2} = {result} into {idx}: {self.intcode[idx]== result}")

    def multiply(self, params):
        m1, m2, idx = params
        m1 = self.find_param(m1)
        m2 = self.find_param(m2)
        idx = self.find_param(idx)

        result = m1 * m2
        self.intcode[idx] = result
        self.index += 4

        if self.debug: print(f">>Inserted {m1} * {m2} = {result} into {idx}: {self.intcode[idx]== result}")

    def input(self, params):
        idx = params[0]
        self.intcode[idx] = self.inputs.pop(0)
        self.index += 2

        if self.debug: print(f">>Inputted {self.intcode[idx]} into index {idx}")

    def output(self, params):
        idx = params[0]
        self.outputs.append(self.intcode[idx])
        self.index += 2

        if self.debug: print(f">>Outputted {self.outputs[-1]}")