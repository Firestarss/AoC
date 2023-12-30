
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    notes = [[list(s) for s in l.split("\n")] for l in f.read().split("\n\n")]

def get_vert_mirror(note, mismatch=0):
    for col in range(1, len(note[0])):
        mismatch_count = 0
        for row in range(len(note)):
            beg_split = note[row][:col][::-1]
            end_split = note[row][col:]

            beg_split = beg_split[:min(len(beg_split), len(end_split))]
            end_split = end_split[:min(len(beg_split), len(end_split))]

            mismatch_count += len([1 for x in range(len(beg_split)) if beg_split[x] != end_split[x]])

        if mismatch_count == mismatch:
            return col
        
    return 0

def get_horiz_mirror(note, mismatch=0):
    for row in range(1, len(note)):
        mismatch_count = 0
        top_split = note[:row][::-1]
        bot_split = note[row:]

        top_split = top_split[:min(len(top_split), len(bot_split))]
        bot_split = bot_split[:min(len(top_split), len(bot_split))]

        for i in range(len(top_split)):
            for j in range(len(top_split[0])):
                if top_split[i][j] != bot_split[i][j]:
                    mismatch_count += 1

        if mismatch_count == mismatch:
            return row
        
    return 0

def part1():
    print(sum([get_vert_mirror(note) for note in notes]) + sum([get_horiz_mirror(note) for note in notes]) * 100)


def part2():
    print(sum([get_vert_mirror(note, 1) for note in notes]) + sum([get_horiz_mirror(note, 1) for note in notes]) * 100)


part1()
part2()