step = 314

def part1():
    idx = 0
    state = [0]

    for i in range(2017):
        idx = (idx + step) % len(state) + 1
        state.insert(idx, i + 1)

    print(state[idx + 1])

def part2():
    idx = 0
    state = 1
    tracker = 0

    for i in range(50000000):
        idx = (idx + step) % state + 1
        state += 1

        if idx == 1:
            tracker = i + 1

    print(tracker)

part1()
part2()