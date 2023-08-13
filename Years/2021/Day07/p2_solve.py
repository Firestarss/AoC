

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[1], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

data = [int(x) for x in data[0].split(",")]

max_crab = max(data)
min_crab = min(data)
cheapest = []

for i in range(max_crab):
    fuel_cost = 0
    for crab in data:
        n = abs(i - crab)
        fuel_cost += n*(n+1)/2

    cheapest.append(fuel_cost)
        
print(min(cheapest))
