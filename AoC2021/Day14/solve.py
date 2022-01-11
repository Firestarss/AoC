from copy import copy
import collections
import numpy as np
import datetime

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    data = file.read().split("\n\n")

template = data[0]
d_pairs = {}
for x in data[1].split("\n"): d_pairs[x[:2]] = x[-1] 

def step(old_dict):
    output = {}
    for pair in old_dict:
        if pair not in d_pairs:
            output[pair] = output.get(pair, 0) + old_dict[pair]
        
        else: # if pair is in d_pairs
            pair_1 = pair[0] + d_pairs[pair]
            pair_2 = d_pairs[pair] + pair[1]
            output[pair_1] = output.get(pair_1, 0) + old_dict[pair]
            output[pair_2] = output.get(pair_2, 0) + old_dict[pair]

    return(output)

def part1(template):
    for j in range(10):
        temp = ""
        for i in range(len(template)-1):
            if template[i:i+2] in d_pairs:
                temp += template[i] + d_pairs[template[i:i+2]]
            else:
                temp += template[i]

        temp += template[-1]
        template = temp

    hist = collections.Counter(template).most_common()
    print(hist[0][1] - hist[-1][1])

def part2(template, iterations=10):
    t_pairs = {}
    for c in range(len(template)-1):
        pair = template[c:c+2]

        if pair not in t_pairs:
            t_pairs[pair] = 1
        else:
            t_pairs[pair] += 1

    for _ in range(iterations):
        t_pairs = step(t_pairs)

    char_count = np.zeros(26, int)
    
    for pair in t_pairs:
        char = pair[0]
        char_count[ord(char) - ord("A")] += t_pairs[pair]

    char_count[ord(template[-1]) - ord("A")] += 1

    print(max(char_count) - min(char_count[char_count > 0]))

part2(copy(template))
part2(copy(template),40)