import string
filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().split("\n")

input = [list(x) for x in input]

def solve():
    cords = [0, input[0].index("|")]
    dir = (1, 0)
    directions = set([(-1, 0),(1, 0),(0, -1),(0, 1)])
    path = []
    count = 0

    while True:
        cords = [cords[0] + dir[0], cords[1] + dir[1]]
        if input[cords[0]][cords[1]] == " ":
            print("".join(path))
            break
        
        if input[cords[0]][cords[1]] == "+":
            reverse = tuple([x * -1 for x in dir])
            possible = directions - set([dir, reverse])

            for temp in possible:
                if input[cords[0] + temp[0]][cords[1] + temp[1]] != " ":
                    dir = temp
                    continue

        if input[cords[0]][cords[1]] in string.ascii_uppercase:
            path.append(input[cords[0]][cords[1]])

        count += 1

    print(count + 1)
    
solve()