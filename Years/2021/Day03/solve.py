with open("input.txt", "r") as infile:
    data = infile.read().strip().split("\n")

def common_bits(bit_strs, most_common = True):
    common_bit_string = ""
    for bit in range(len(bit_strs[0])):
        counter = [0,0] # [0,1]
        for line in data:
            if line[bit] == "0": counter[0] += 1
            else: counter[1] += 1
        if not most_common: counter = [count * -1 for count in counter]
        common_bit_string += "0" if counter[0] > counter[1] else "1"

    return common_bit_string

def part1():
    print(int(common_bits(data),2) * int(common_bits(data, False),2))

part1()
