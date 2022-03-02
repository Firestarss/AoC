import collections
import string

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input = [[x[:x.rfind("-")], int(x[x.rfind("-") + 1 : x.find("[")]), x[x.find("[") + 1 : x.find("]")]] for x in input]

def shift(code, value):
    letters = string.ascii_lowercase
    output = list()
    
    for letter in code:
        if letter == "-":
            output.append(" ")
            continue

        output.append(letters[(letters.index(letter) + value) % len(letters)])
    
    output = "".join(output)

    return output

def solve():
    total = 0
    north_pole = 0

    for room in input:
        if "north" in shift(room[0], room[1]):
            north_pole = room[1]

        room[0] = room[0].replace("-", "")
        tops = [(-n,c) for c,n in collections.Counter(room[0]).most_common()]
        ranked = ''.join(c for n,c in sorted(tops))

        if ranked[:5] == room[2]:
            total += room[1]

    print(total)
    print(north_pole)


solve()