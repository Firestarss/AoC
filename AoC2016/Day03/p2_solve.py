import re

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = [int(x) for x in re.split("\s+",line.strip())]
        data.append(temp)

possible = 0
for i in range(len(data)):
    t1 = []
    t2 = []
    t3 = []
    if i % 3 == 0:
        t1 = [data[i][0], data[i + 1][0], data[i + 2][0]]
        t2 = [data[i][1], data[i + 1][1], data[i + 2][1]]
        t3 = [data[i][2], data[i + 1][2], data[i + 2][2]]

        for t in [t1, t2, t3]:
            t.sort()
            if t[0] + t[1] > t[2]:
                possible += 1

print(possible)
