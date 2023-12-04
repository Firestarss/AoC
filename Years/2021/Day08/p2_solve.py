import re

input_file = ["input.txt", "test_input.txt", "mini_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

def overlap(a, b):
    counter = 0
    for x in a:
        if x in b:
            counter += 1

    return counter

def order(input):
    sorted_characters = sorted(input)
    a_string = "".join(sorted_characters)

    return a_string

temp_data = []
for point in data:
    temp = []
    point = point.split("|")
    temp.append(point[0].strip().split(" "))
    temp.append(point[1].strip().split(" "))

    temp_data.append(temp)

data = temp_data

total = 0
for point in data:
    codewords = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:""}

    for code in point[0]:
        if len(code) == 2:
            codewords[1] = code
        if len(code) == 4:
            codewords[4] = code
        if len(code) == 3:
            codewords[7] = code
        if len(code) == 7:
            codewords[8] = code

    for code in point[0]:
        if len(code) == 5:
            if overlap(codewords[1], code) == 2:
                codewords[3] = code
            elif overlap(codewords[4], code) == 3:
                codewords[5] = code
            else:
                codewords[2] = code

    for code in point[0]:
        if len(code) == 6:
            if overlap(code, codewords[1]) == 1:
                codewords[6] = code
            elif overlap(code, codewords[5]) == 4:
                codewords[0] = code
            else:
                codewords[9] = code

    rcodewords = dict((order(v),k) for k,v in codewords.items())

    local_output = ""

    for codeword in point[1]:
        local_output += str(rcodewords[order(codeword)])
 
    total += int(local_output)

print(total)