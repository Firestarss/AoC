from collections import Counter
input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

def part1():
    two_count = 0
    three_count = 0

    for word in input:
        temp_count = Counter(word).most_common()
        if len([x for x in temp_count if x[1] == 2]) > 0: two_count += 1
        if len([x for x in temp_count if x[1] == 3]) > 0: three_count += 1

    print(two_count * three_count)

def part2():
    for i in range(len(input)):
        curi = input[i]

        for j in range(i, len(input)):
            diff = 0
            curj = input[j]

            for k in range(len(curi)):
                if diff > 1:
                    break

                if curi[k] != curj[k]:
                    diff += 1

            if diff == 1:
                print("".join([curi[x] for x in range(len(curi)) if curi[x] == curj[x]]))

part1()
part2()