

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        data.append(int(line.strip()))

count = 0
for i in range(len(data)-3):
    if sum(data[i:i+3]) < sum(data[i+1:i+4]):
        count += 1

print(count)