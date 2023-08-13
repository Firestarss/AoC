from functools import reduce

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input_s = infile.read().strip()

input = [int(x) for x in input_s.split(",")]

def part1(input):
    ls = list(range(256))
    pos = 0
    skip = 0

    for i_length in input:
        temp = ls[pos:] + ls[:pos]
        rev = temp[:i_length][::-1] + temp[i_length:]
        ls = rev[-pos:] + rev[:-pos]

        pos = (pos + i_length + skip) % len(ls)
        skip += 1

    print(ls[0] * ls[1])
        
def part2(input):
    ls = list(range(256))
    lengths = [ord(x) for x in input] + [17, 31, 73, 47, 23]

    pos = 0
    skip = 0

    for _ in range(64):
        for i_length in lengths:
            temp = ls[pos:] + ls[:pos]
            rev = temp[:i_length][::-1] + temp[i_length:]
            ls = rev[-pos:] + rev[:-pos]

            pos = (pos + i_length + skip) % len(ls)
            skip += 1

    hash = "".join([hex(x)[2:].zfill(2) for x in [reduce(lambda i, j: int(i) ^ int(j), group) for group in [ls[i:i + 16] for i in range(0, len(ls), 16)]]])
    print(hash)

part1(input)
part2(input_s)