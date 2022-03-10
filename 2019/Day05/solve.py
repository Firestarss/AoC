import sys
sys.path.append('../')
from intcode import Interperator

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input = [x for x in input]

intint = Interperator(True)
intint.add_input(88)
intint.load_intcode([3,0,4,0,99])
intint.compute()
print(intint.get_outputs())