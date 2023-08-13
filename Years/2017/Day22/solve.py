input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

s_infected = set()
l_infected = dict()
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[j][i] == "#":
            s_infected.add((i,j))
            l_infected[(i,j)] = "i" # clean (0), weak (1), flagged (2), infected (3)


def part1():
    headings = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
    cur = (len(input[0])//2, len(input)//2)
    heading = 0
    infections = 0

    for _ in range(10000):
        if cur in s_infected:
            heading += 1
            s_infected.remove(cur)
        else:
            heading -= 1
            s_infected.add(cur)
            infections += 1

        heading = heading % 4
        cur = (cur[0] + headings[heading][0], cur[1] + headings[heading][1])

    print(infections)

def part2():
    headings = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
    cur = (len(input[0])//2, len(input)//2)
    heading = 0
    infections = 0
    debug = False

    for _ in range(10000000):
        if cur not in l_infected or l_infected[cur] == "c":
            if debug: print(cur, "c -> w")
            l_infected[cur] = "w"
            heading -= 1
        
        elif l_infected[cur] == "w":
            if debug: print(cur, "w -> i")
            l_infected[cur] = "i"
            infections += 1

        elif l_infected[cur] == "i":
            if debug: print(cur, "i -> f")
            l_infected[cur] = "f"
            heading += 1

        elif l_infected[cur] == "f":
            if debug: print(cur, "f -> c")
            l_infected[cur] = "c"
            heading += 2

        heading = heading % 4
        cur = (cur[0] + headings[heading][0], cur[1] + headings[heading][1])

    print(infections)

part1()
part2()