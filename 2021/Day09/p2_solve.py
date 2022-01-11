import numpy as np

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append([int(x) for x in list(temp)])

data = np.array(data)

data = np.pad(data, pad_width=1, mode='constant', constant_values=10)

lows = []
for row in range(len(data)):
    for col in range(len(data[0])):
        low = True
        if data[row][col] != 10:
            for adj in [(0,1),(1,0),(0,-1),(-1,0)]:
                point = data[row + adj[0]][col + adj[1]]
                if point <= data[row][col]:
                    low = False
        
            if low:
                lows.append((row,col))

basins = []

for low in lows:
    visited = [low]
    queue = [low]

    while queue:
        cur = queue.pop(0)
        for adj in [(0,1),(1,0),(0,-1),(-1,0)]:
            looking = (cur[0] + adj[0],cur[1] + adj[1])
            if data[looking[0]][looking[1]] < 9 and looking not in visited:
                queue.append(looking)
                visited.append(looking)

    basins.append(len(visited))

basins.sort(reverse=True)

total = 1

for i in range(3):
    total *= basins[i]

print(total)