input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def part1():
    targets = [20, 60, 100, 140, 180, 220]
    cycles = 1
    x = 1
    signals = []

    for line in lines:
        if line.startswith("addx"):
            for _ in range(2):
                if cycles in targets: signals.append(x * cycles)
                cycles += 1
            x += int(line.split(" ")[1])
        else:
            if cycles in targets: signals.append(x * cycles)
            cycles += 1

    print(sum(signals))


def part2():
    cycles = 0
    x = 1
    resolution = (40, 6)
    display = []

    for line in lines:
        if line.startswith("addx"):
            for _ in range(2):
                if abs(cycles % 40 - x) <= 1: display.append("█")
                else: display.append(" ")
                cycles += 1
            x += int(line.split(" ")[1])
        else:
            if abs(cycles % 40 - x) <= 1: display.append("█")
            else: display.append(" ")
            cycles += 1
            
    for i in range(resolution[1]):
        print("".join(display[i * 40 : i * 40 + 40]))

part1()
part2()