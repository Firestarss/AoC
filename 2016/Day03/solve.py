import re
import copy

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = [int(x) for x in re.split("\s+",line.strip())]
        data.append(temp)

def part1(local_data):
    local_data = copy.deepcopy(local_data)
    possible = 0
    for point in local_data:
        point.sort()
        if point[0] + point[1] > point[2]:
            possible += 1

    print(possible)

def part2(data):
    temp_data = []
    for i in range(len(data)):
        if i % 3 == 0:
            for j in range(3):
                temp_data.append([data[i][j], data[i+1][j], data[i+2][j]])
    
    part1(temp_data)

part1(data) # 982
part2(data) # 1826