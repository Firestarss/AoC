from collections import defaultdict

input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

ends = set([(int(x.split("/")[0]),int(x.split("/")[1])) for x in input])
connections = defaultdict(set)

for end in ends:
    connections[end[0]].add(end[1])
    connections[end[1]].add(end[0])

def sum_path(path):
    return sum([sum(x) for x in path])


def solve():
    paths = {((0,0),(0,0))}
    changed = True
    
    while changed:
        changed = False
        to_add = set()
        to_remove = set()

        for path in paths:
            loose_end = path[-1][-1]

            for connection in connections[loose_end]:
                if (loose_end, connection) in path or (connection, loose_end) in path: continue
                else:
                    next_node = (loose_end, connection)
                    to_add.add(tuple(list(path) + [next_node]))
                    to_remove.add(path)
                    changed = True

        paths = paths.union(to_add)
        paths = paths.difference(to_remove)

    print(max([sum_path(x) for x in paths]))
    print(sorted([(len(x), sum_path(x)) for x in paths])[-1][-1])

solve()