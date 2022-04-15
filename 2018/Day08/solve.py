from copy import copy
input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = [int(x) for x in f.read().strip().split(" ")]

def solve():
    child_stack = [input[0]]
    meta_stack = [input[1]]
    data = []
    data2 = 0
    child_values = [[]]
    meta_values = [[]]
    i = 2

    while i < len(input) or child_stack:
        child_stack[-1] -= 1
        child_stack.append(input[i])
        meta_stack.append(input[i+1])

        child_values.append([])
        meta_values.append([])
        i += 2

        while child_stack and child_stack[-1] == 0:
            child_stack.pop()
            num_data = meta_stack.pop()
            data += input[i:i+num_data]

            meta_values[-1] += input[i:i+num_data]
            i += num_data

            last_child = child_values.pop()
            last_meta = meta_values.pop()
            
            if last_child:
                value = [last_child[j - 1] for j in last_meta if 1 <= j <= len(last_child)]
                value = sum(value)
            else:
                value = sum(last_meta)

            if child_values:
                child_values[-1].append(value)
            else:
                data2 = value

    print(sum(data))
    print(data2)

solve()