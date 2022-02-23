def compute(input):
    i = 0
    while i < len(input):
        step = 0
        code = input[i]
        if code == 99:
            break

        if code == 1:
            target_index = input[i + 3]
            input[target_index] = input[input[i + 1]] + input[input[i + 2]]
            step = 4

        if code == 2:
            target_index = input[i + 3]
            input[target_index] = input[input[i + 1]] * input[input[i + 2]]
            step = 4

        i = i + step

    return input