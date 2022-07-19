from collections import Counter
import re
import math

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [int(a.strip()) for a in f.readlines()]
lines = lines + [0, max(lines) + 3]
lines.sort()

def tribonacci(n):
    if n <= 2: return [1, 1, 2][n]

    return (tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3))

def solve():
    diffs = [lines[i+1] - lines[i] for i in range(len(lines)-1)]
    diff_counter = Counter(diffs)
    print(diff_counter[1]*diff_counter[3])
    
    diffs = "".join(map(str, diffs))
    clusters = [len(x) for x in re.findall("1+", diffs)]

    trib = [tribonacci(x) for x in clusters]
    print(math.prod(trib))


solve()