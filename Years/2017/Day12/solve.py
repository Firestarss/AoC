with open("input.txt", "r") as infile:
    input = [x.split(" <-> ") for x in infile.read().strip().split("\n")]

nodes = {key:value.split(", ") for key,value in input}

def solve():
    groups = 0

    while nodes.keys():
        q, v = [next(iter(nodes))], [next(iter(nodes))]

        while q:
            cur = q.pop(0)

            for child in nodes[cur]:
                if child not in v:
                    q.append(child)
                    v.append(child)
            
        groups += 1
        for child in v:
            del nodes[child]

        if v[0] == "0":
            print(len(v))

    print(groups)

solve()