filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split(",")

input = [[x[0]] + x[1:].split("/") for x in input]

def dance(letters):
    for inst in input:
        if inst[0] == "s":
            int1 = int(inst[1])
            letters = letters[-int1:] + letters[:-int1]

        if inst[0] == "x":
            int1 = int(inst[1])
            int2 = int(inst[2])

            letters = list(letters)
            temp = letters[int1]
            letters[int1] = letters[int2]
            letters[int2] = temp

            letters = "".join(letters)

        if inst[0] == "p":
            idx1 = letters.index(inst[1])
            idx2 = letters.index(inst[2])

            letters = list(letters)
            temp = letters[idx1]
            letters[idx1] = letters[idx2]
            letters[idx2] = temp
            
            letters = "".join(letters)

    return letters

def part1():
    print(dance("abcdefghijklmnop"))

def part2():
    results = []
    letters = "abcdefghijklmnop"

    for i in range(1000000000):
        to_add = dance(letters)

        if to_add in results:
            print(results[1000000000 % i - 1])
            break
        else:
            results.append(to_add)
            letters = to_add

part1()
part2()