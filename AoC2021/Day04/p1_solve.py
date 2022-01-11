import re
import numpy as np

class Board():

    def __init__(self, board):
        self.bit_board = np.zeros((5,5))
        self.board = np.zeros((5,5))

        for row in range(5):
            for col in range(5):
                self.board[row][col] = int(board[row][col])

    def get_bit_board(self):
        return self.bit_board

    def get_board(self):
        return self.board

    def display(self):
        print("-"*40)
        for i in range(5):
            print(str(self.board[i]) + "\t" + str(self.bit_board[i]))
        print("-"*40)

    def mark(self, value):
        if value in self.board:
            coords = np.where(self.board == value)
            coords = list(zip(coords[0], coords[1]))[0]
            self.bit_board[coords[0]][coords[1]] = 1

    def is_solved(self):
        if 5 in [sum(self.bit_board[:,x]) for x in range(5)]:
            # print("vert")
            return True

        if 5 in [sum(self.bit_board[x,:]) for x in range(5)]:
            # print("horiz")
            return True

        return False


if __name__ == "__main__":

    input_file = ["input.txt", "test_input.txt"]

    data = []
    with open(input_file[0], "r") as file:
        for line in file:
            temp = line.strip()
            data.append(temp)

    draw_order = [int(x) for x in data[0].split(",")]
    boards = []

for i in range(len(data)):
    if data[i] == "":
        temp = [re.split("\s+", data[i+1+x]) for x in range(5)]
        boards.append(Board(temp))

solved = False
for draw in draw_order:
    if solved:
        break

    for board in boards:
        board.mark(draw)
        
        if board.is_solved():
            solved = True
            row, col = np.where(board.get_bit_board() == 0)
            unmarked_sum = sum([board.get_board()[row[x]][col[x]] for x in range(len(row))])
            answer = unmarked_sum * draw
            print(int(answer))

            break