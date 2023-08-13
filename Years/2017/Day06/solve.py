filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input = [int(x) for x in input[0].split("\t")]

def redistribute(input):
    i_max = input.index(max(input))
    val = input[i_max]

    input[i_max] = 0

    while val:
        i_max += 1
        input[i_max % len(input)] += 1
        val -= 1

    return input
    
def solve(input):
    v = set()
    counter = 0
    pt2_start = 0
    seen = []
    while True:
        counter += 1
        input = redistribute(input)
        if tuple(input) in v and not seen:
            seen = tuple(input)
            pt2_start = counter
            print(counter)
        elif tuple(input) in v and tuple(input) == seen:
            print(counter - pt2_start)
            break
        else:
            v.add(tuple(input))

solve(input)