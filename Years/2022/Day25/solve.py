input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def part1():
    dec_sum = sum([snafu_to_decimal(x) for x in lines])
    decimal_to_snafu(dec_sum)

def snafu_to_decimal(num):
    num = [x for x in str(num)]
    for i in range(len(num)):
        if num[i] == "-": num[i] = -1
        if num[i] == "=": num[i] = -2

    total = 0
    place = 1

    while num:
        cur = num.pop()
        total += (int(cur) * place)
        place *= 5

    return total

def decimal_to_snafu(num):
    mini = num * 3
    length = 0
    for i in range(len(str(num)) * 3):
        test = "2" + "0" * i
        if abs(num - snafu_to_decimal(test)) <= mini:
            mini = abs(num - snafu_to_decimal(test))
            length = i+1

    output = ["0" for _ in range(length)]

    for i in range(len(output)):
        mini = abs(num * 3)
        to_add = "0"

        for value in ["2", "1", "0", "-", "="]:
            output[i] = value
            if abs(num - snafu_to_decimal("".join(output))) < mini:
                mini = abs(num - snafu_to_decimal("".join(output)))
                to_add = value

        output[i] = to_add
    print("".join(output))

part1()