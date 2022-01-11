

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

data = [int(x) for x in data[0].split(",")]

def step(data):
    temp = []
    for fish in data:
        if fish > 0:
            temp.append(fish - 1)
        else:
            temp += [6,8]

    return temp

for i in range(80):
    print(i)
    data = step(data)

print(len(data))