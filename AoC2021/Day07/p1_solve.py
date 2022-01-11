

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

data = [int(x) for x in data[0].split(",")]

max_crab = max(data)
min_crab = min(data)
cheapest = max_crab * len(data)

for i in range(max_crab-min_crab):
    temp = 0
    for crab in data:
        temp += abs((i+min_crab) - crab)

    if temp < cheapest:
        cheapest = temp

print(cheapest)