import numpy as np
from copy import deepcopy

input_files = ["input.txt", "test_input.txt"]

with open(input_files[0], 'r') as f:
    data =  [a.strip() for a in f.readlines()]

iea = data[0]
image = np.array([list(x) for x in data[2:]])
outside = '.'

def get_char(grid):

    flat = grid.flatten()
    flat[flat == "."] = 0
    flat[flat == "#"] = 1
    
    bitstring = "".join(flat)
    value = int(bitstring, 2)

    return iea[value]

def step(img, outside, iea=iea):
    img = np.pad(img, 2, 'constant', constant_values = outside)
    new_img = np.zeros((img.shape[0] - 2, img.shape[1] - 2), dtype=str)

    for y in range(new_img.shape[0]):
        for x in range(new_img.shape[1]):
            grid = img[y:y+3, x:x+3]

            new_img[y][x] = get_char(grid)
    return new_img

def simulate(image, outside, iter):
    for i in range(iter):
        image = step(image, outside)
        outside = get_char(np.array(list(outside*9)).reshape((3,3)))

    print(np.count_nonzero(image == "#"))

def part1(image, outside):
    simulate(image, outside, 2)

def part2(image, outside):
    simulate(image, outside, 50)
    
part1(deepcopy(image), deepcopy(outside))
part2(deepcopy(image), deepcopy(outside))