def part1(data):
    print(sum(1 if char == '(' else -1 for char in data))

def part2(data):
    floor = 0
    for i, char in enumerate(data):
        floor = floor + 1 if char == "(" else floor - 1
        if floor < 0:
            print(i + 1)
            break

if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        data = file.read()

    part1(data)
    part2(data)

