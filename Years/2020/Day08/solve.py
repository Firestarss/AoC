import copy

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip().split(" ") for a in f.readlines()]

lines = [[a[0], int(a[1])] for a in lines]

def is_infinite(change_idx):
    local_lines = copy.deepcopy(lines)
    if change_idx != -1:
        if local_lines[change_idx][0] == "nop":
            local_lines[change_idx][0] = "jmp"
        else:
            local_lines[change_idx][0] = "nop"

    acc = 0
    idx = 0
    visited = set()

    while idx < len(local_lines):
        if idx in visited: return (True, acc)
        visited.add(idx)
        if local_lines[idx][0] == "acc": acc += local_lines[idx][1]
        if local_lines[idx][0] == "jmp": idx += local_lines[idx][1] - 1
        idx += 1

    return (False, acc)


def part1():
    print(is_infinite(-1)[1])

def part2():
    changeable = [x for x in range(len(lines)) if lines[x][0] in ["nop", "jmp"]]
    acc_scores = sorted([is_infinite(x) for x in changeable])
    print(acc_scores[0][1])

part1()
part2()