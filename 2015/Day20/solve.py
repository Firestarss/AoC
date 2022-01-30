def part1and2(input):
    houses1 = [0] * (input//10)
    houses2 = [0] * (input//10)
    for i in range(1, input//10):
        count = 0
        for j in range(i, input//10, i):
            houses1[j] += i * 10
            if count < 50:
                houses2[j] += i * 11
                count += 1

    for i in range(input//10):
        if houses1[i] >= input:
            print(i)
            break

    for i in range(input//10):
        if houses2[i] >= input:
            print(i)
            break

input = 29000000
part1and2(input)