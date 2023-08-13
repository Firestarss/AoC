

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip().split(" -> ") for a in f.readlines()]
    rocks = set()

    for line in lines:
        for i in range(len(line) - 1):
            c1 = line[i].split(",")
            c2 = line[i+1].split(",")

            xs = [int(c1[0]), int(c2[0])]
            ys = [int(c1[1]), int(c2[1])]

            if len(set(xs)) == 1:
                rocks.update(set([(xs[0],y) for y in range(min(ys), max(ys) + 1)]))

            if len(set(ys)) == 1:
                rocks.update(set([(x,ys[0]) for x in range(min(xs), max(xs) + 1)]))

def part1():
    sand = set()
    spawn = (500,0)
    bottom = max([cord[1] for cord in rocks])
    running = True
    while running:
        f_sand = list(spawn)
        falling = True
        while falling:
            old = f_sand[:]
            blocked = sand.union(rocks)
            if (f_sand[0], f_sand[1] + 1) not in blocked: f_sand[1] += 1
            elif (f_sand[0] - 1, f_sand[1] + 1) not in blocked: f_sand = [f_sand[0] - 1, f_sand[1] + 1]
            elif (f_sand[0] + 1, f_sand[1] + 1) not in blocked: f_sand = [f_sand[0] + 1, f_sand[1] + 1]

            if f_sand == old:
                falling = False
                sand.add(tuple(f_sand))

            elif f_sand[1] > bottom: falling = running = False

    print(len(sand))


def part2():
    floor = max([cord[1] for cord in rocks]) + 2
    rock_num = len(rocks)
    q = [(500,0)]
    v = rocks.union(q[-1])
    while q:
        cur = q.pop(0)
        for point in [(-1,1), (0,1), (1,1)]:
            n = (cur[0] + point[0], cur[1] + point[1])
            if n not in v and n[1] < floor:
                v.add(n)
                q.append(n)

    print(len(v) - rock_num - 1)

part1()
part2()