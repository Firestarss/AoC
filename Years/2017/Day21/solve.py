import numpy as np
input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

def reflections(instruction, i_dict):
    instruction = instruction.replace("#", "1").replace(".", "0").replace("/", "").split(" => ")
    question = np.asarray([x for x in instruction[0]], dtype=str)
    answer = np.asarray([x for x in instruction[1]], dtype=int)

    for value in [question, answer]:
        if value.size == 4:
            value.resize((2,2))
        elif value.size == 9:
            value.resize((3,3))
        elif value.size == 16:
            value.resize((4,4))

    for _ in range(4):
        question = np.rot90(question)
        lr_flip = np.fliplr(question)
        ud_flip = np.flipud(question)
        i_dict["".join(question.flatten())] = answer
        i_dict["".join(lr_flip.flatten())] = answer
        i_dict["".join(ud_flip.flatten())] = answer

    return i_dict


start = ".#./..#/###"
start = start.replace("#", "1").replace(".", "0").replace("/", "")
start = np.asarray([x for x in start], dtype=int).reshape((3,3))

def solve(iterations):
    board = np.copy(start)

    instructions = {}
    for line in input:
        instructions = reflections(line, instructions)

    for _ in range(iterations):
        to_stack = []
        if board.shape[0] % 2 == 0:
            for i in range(board.shape[0]//2):
                temp_stack = []
                for j in range(board.shape[1]//2):
                    key = "".join([str(x) for x in board[i*2:i*2+2, j*2:j*2+2].flatten()])
                    temp_stack.append(instructions[key])
                to_stack.append(temp_stack)

        else:
            for i in range(board.shape[0]//3):
                temp_stack = []
                for j in range(board.shape[1]//3):
                    key = "".join([str(x) for x in board[i*3:i*3+3, j*3:j*3+3].flatten()])
                    temp_stack.append(instructions[key])
                to_stack.append(temp_stack)

        rows = []
        for col in to_stack:
            rows.append(np.hstack(tuple(col)))

        board = np.vstack(tuple(rows))

    print(np.count_nonzero(board == 1))

solve(5)
solve(18)