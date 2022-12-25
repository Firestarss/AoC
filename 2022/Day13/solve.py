import ast
import time
input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip().split("\n") for a in f.read().split("\n\n")]
    lines = [[ast.literal_eval(a) for a in b] for b in lines]

def part1():
    idx_count = 1
    total = 0

    for line in lines:
        if check_validity(line[0], line[1]):
            total +=idx_count

        idx_count += 1

    print(total)

def part2():
    sort = [[[6]], [[2]]]
    for line in lines:
        sort.append(line[0])
        sort.append(line[1])

    changed = True
    while changed:
        changed = False
        for i in range(len(sort)-1):
            if not check_validity(sort[i], sort[i + 1]):
                temp = sort[i]
                sort[i] = sort[i+1]
                sort[i+1] = temp
                changed = True

    decoder_key = 1
    for i, packet in enumerate(sort):
        if packet in [[[6]], [[2]]]:
            decoder_key *= i + 1

    print(decoder_key)

def get_next(side, si):
    cur = side
    for i in si:
        if isinstance(cur, int): return cur
        cur = cur[i]

    return cur

def check_validity(l,r):
    li = [0]
    ri = [0]
    ll = [len(l)]
    rl = [len(r)]

    while ll or rl:
        while li[-1] >= ll[-1] or ri[-1] >= rl[-1]:
            if (ll[-1] - li[-1]) < (rl[-1] - ri[-1]): return True
            if (ll[-1] - li[-1]) > (rl[-1] - ri[-1]): return False
            li.pop()
            ll.pop()
            ri.pop()
            rl.pop()
            li[-1] += 1
            ri[-1] += 1

        curl = get_next(l, li)
        curr = get_next(r,ri)

        if (type(curl) is not type(curr)):
            if isinstance(curl, int): curl = [curl]
            else: curr = [curr]

        if isinstance(curl, int) and isinstance(curr, int):
            if curl < curr: return True
            elif curl > curr: return False
            li[-1] += 1
            ri[-1] += 1

        elif isinstance(curl, list) and isinstance(curr, list):
            li.append(0)
            ri.append(0)
            ll.append(len(curl))
            rl.append(len(curr))

    
part1()
part2()