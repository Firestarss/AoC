from functools import reduce

input = "ljoxqyyw"
# input = "flqrgnkx"
grid = []

def knot_hash(input):
    ls = list(range(256))
    lengths = [ord(x) for x in input] + [17, 31, 73, 47, 23]

    pos = 0
    skip = 0

    for _ in range(64):
        for i_length in lengths:
            temp = ls[pos:] + ls[:pos]
            rev = temp[:i_length][::-1] + temp[i_length:]
            ls = rev[-pos:] + rev[:-pos]

            pos = (pos + i_length + skip) % len(ls)
            skip += 1

    hash = "".join([hex(x)[2:].zfill(2) for x in [reduce(lambda i, j: int(i) ^ int(j), group) for group in [ls[i:i + 16] for i in range(0, len(ls), 16)]]])
    return hash

def part1():
    for i in range(128):
        hash = knot_hash(input + "-" + str(i))
        hash = bin(int(hash, 16))[2:].zfill(128)
        grid.append(hash)

    print(sum([x.count("1") for x in grid]))

def part2():
    ones = []

    for i in range(128):
        for j in range(128):
            if grid[i][j] == "1":
                ones.append((i,j))

    count = 0

    while ones:
        count += 1
        q = [ones.pop(0)]
        
        while q:
            cur = q.pop(0)

            for adj in [(1,0), (-1,0), (0,1), (0,-1)]:
                check = (cur[0] + adj[0], cur[1] + adj[1])
                if check in ones:
                    q.append(check)
                    ones.remove(check)

    print(count)


part1()
part2()