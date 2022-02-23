filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input = [int(x) for x in input]

def fuel_weight(mass):
    total = []
    while mass > 0:
        total.append(max(0, mass := mass // 3 - 2))

    return sum(total)

print(sum([x//3-2 for x in input]))
print(sum([fuel_weight(x) for x in input]))