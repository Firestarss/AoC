

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [list(map(int, a.strip().split())) for a in f.readlines()]

def solve():
    totals = [coctail_shaker_extend_sequence(seq) for seq in lines]

    print(sum([x[1] for x in totals]))
    print(sum([x[0] for x in totals]))


def coctail_shaker_extend_sequence(seq):
    levels = [seq]

    while levels[-1][-1] != 0 and len(set(levels[-1])) != 1:
        new_level = []
        for i in range(len(levels[-1]) - 1):
            new_level.append(levels[-1][i + 1] - levels[-1][i])
        levels.append(new_level)

    levels.append([0 for _ in range(len(levels[-1]))])

    for i in range(len(levels) - 1):
        cur_level = -2 - i
        levels[cur_level].append(levels[cur_level][-1] + levels[cur_level + 1][-1])
        levels[cur_level].insert(0, levels[cur_level][0] - levels[cur_level + 1][0])

    return (levels[0][0], levels[0][-1])

solve()