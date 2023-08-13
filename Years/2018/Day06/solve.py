import re
import numpy as np

input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip()

min_int = 0 - min(list(map(int, re.findall(r"\d+", input))))
max_int = max(list(map(int, re.findall(r"\d+", input)))) - min_int

input = input.split("\n")
input = [(int(x.split(", ")[0]), int(x.split(", ")[1])) for x in input]

def solve():
    grid = np.zeros(max_int, dtype=int)
    sizes = {key:0 for key in input}
    p2_region_size = 0
    infinites = set()

    for i in range(min_int, max_int):
        for j in range(min_int, max_int):
            min_dist = max_int  * 5

            distances = [abs(i-point[0]) + abs(j-point[1]) for point in input]
            min_dist = min(distances)

            if distances.count(min_dist) == 1:
                input_idx = distances.index(min_dist)
                closest_point = input[input_idx]
                sizes[closest_point] += 1

                if i==min_int or i==max_int-1 or j==min_int or j==max_int-1:
                    infinites.add(closest_point)

            if sum(distances) < 10000:
                p2_region_size += 1

    print(max([sizes[x] for x in sizes if x not in infinites]))
    print(p2_region_size)


solve()