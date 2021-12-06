

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

data = [int(x) for x in data[0].split(",")]

hist = []

for i in range(9):
    hist.append(data.count(i))


def step(data):
    temp = [0 for x in range(len(data))]

    reset = 0
    for i in range(len(data)):
        if i < 9:
            temp[i-1] = data[i]

    temp[6] = data[0] + data[7]
    temp[8] = data[0]
    
    return temp

print(hist)
for i in range(256):
    hist = step(hist)

print(sum(hist) == 1622533344325)