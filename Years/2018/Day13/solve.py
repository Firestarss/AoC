input_files = ["input.txt", "test_input.txt", "test_input2.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().replace("\\", "c").replace("/", "c").split("\n")

input = [list(x) for x in input]
map = {}
carts = {}
directions = {">":0, "^":90, "<":180, "v":270}

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] in "<>v^":
            if input[i][j] in "<>":
                carts[(j,i)] = directions[input[i][j]]
                map[(j,i)] = "-"
            if input[i][j] in "v^":
                carts[(j,i)] = directions[input[i][j]]
                map[(j,i)] = "|"
        else:
            map[(j,i)] = input[i][j]

temp = dict()
for count, value in enumerate(carts):
    temp[count] = [value, carts[value], 0] # pos, heading, turns
carts = temp

def get_queue(carts):
    carts = sorted([[carts[x][0],x] for x in carts], key=lambda e: (e[0][1], e[0][0]))
    queue = [x[1] for x in carts]
    return queue

def move(id, carts):
    moves = {0:(1,0), 90:(0,-1), 180:(-1,0), 270:(0,1)}
    intersection = {0:90, 1:0, 2:-90}
    if id in carts:
        cur = carts[id]
    else:
        return
    cur[0] = (cur[0][0] + moves[cur[1]][0], cur[0][1] + moves[cur[1]][1])

    if map[cur[0]] == "c":
        if cur[1] in [0, 180]:
            above = (cur[0][0], cur[0][1] - 1)
            if above in map and map[above] in "|+":
                cur[1] = 90
            else:
                cur[1] = 270
        elif cur[1] in [90, 270]:
            right = (cur[0][0] + 1, cur[0][1])
            if right in map and map[right] in "-+":
                cur[1] = 0
            else:
                cur[1] = 180

    if map[cur[0]] == "+":
        cur[1] = (cur[1] + intersection[cur[2] % 3]) % 360
        cur[2] += 1

def get_collision(cart_id, carts):
    cart_pos_list = [carts[x][0] for x in carts]
    cart_pos_set = set(cart_pos_list)

    if len(cart_pos_list) == len(cart_pos_set):
        return False

    else:
        crash_pos = carts[cart_id][0]
        crashed_carts = [x for x in carts if carts[x][0] == crash_pos]
        return crashed_carts

def solve(carts):
    first_crash = False
    running = True
    while running:
        if count > 16: running = False
        queue = get_queue(carts)
        for cart in queue:
            move(cart, carts)
            crashes = get_collision(cart, carts)
            if crashes:
                if not first_crash:
                    print(f"{carts[cart][0][0]},{carts[cart][0][1]}")
                    first_crash = True

                for crash in crashes:
                    del carts[crash]

                if len(carts) < 2:
                    last = list(carts.keys())[0]
                    print(f"{carts[last][0][0]},{carts[last][0][1]}")
                    running = False
                    break

solve(carts)