from itertools import combinations

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [int(a.strip()) for a in f.readlines()]

window = 25
def solve():
    for i in range(window, len(lines)):
        sums = {sum(x) for x in combinations(lines[i-window:i], 2)}
        if lines[i] not in sums:
            first_wrong = lines[i]
            print(first_wrong)
            break
    
    weakness = 0
    for i in range(len(lines)):
        running_sum = 0
        for j in range(i, len(lines)):
            running_sum += lines[j]
            if running_sum == first_wrong:
                weakness = min(lines[i:j]) + max(lines[i:j])
                break
        if weakness:
            break

    print(weakness)

solve()