

input_file = ["input.txt", "test_input.txt"]

with open(input_file[0], "r") as file:
    data = list(map(int, file.read().strip().split("\n")))

def part1(data):
    prev = data[0]
    count = 0

    for line in data:
        if line > prev: count += 1
        prev = line

    return count

def part2():
    sum_data = [sum(data[i:i+3]) for i in range(len(data) - 2)]
    return part1(sum_data)

print(part1(data))
print(part2())
