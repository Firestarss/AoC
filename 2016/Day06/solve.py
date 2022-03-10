from collections import Counter

filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

def solve():
    pos_letters = {key:[] for key in range(len(input[0]))}

    for line in input:
        for char_idx in range(len(line)):
            pos_letters[char_idx].append(line[char_idx])

    print("".join([Counter(pos_letters[x]).most_common(1)[0][0] for x in range(len(input[0]))]))
    print("".join([Counter(pos_letters[x]).most_common()[-1][0] for x in range(len(input[0]))]))

solve()