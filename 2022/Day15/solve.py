import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines = [list(map(int, re.findall('-?[0-9]+', a))) for a in f.readlines()]
    sensors = {(l[0], l[1]):abs(l[0]-l[2]) + abs(l[1]-l[3]) for l in lines}
    beacons = {(b[2],b[3]) for b in lines}

def part1():
    y = 10 if file == 1 else 2000000
    left_bound = min([s[0] - sensors[s] for s in sensors])
    right_bound = max([s[0] + sensors[s] for s in sensors])
    not_occupied = 0
    points = []
    p = None

    for i in range(left_bound, right_bound):
        poi = (i, y)
        if poi in beacons:
            continue

        if p and manhattan(poi[0], poi[1], p[0], p[1]) <= sensors[p]:
            not_occupied += 1
            points.append(poi)
            continue

        for s in sensors:
            if manhattan(poi[0], poi[1], s[0], s[1]) <= sensors[s]:
                not_occupied += 1
                points.append(poi)
                p = s
                break

    print(not_occupied)

def part2():
    bound = 20 if file == 1 else 4000000
    edges = set()
    for s in sensors:
        dist = sensors[s]
        c = [(s[0] + dist, s[1]),
             (s[0] - dist, s[1]),
             (s[0], s[1] + dist),
             (s[0], s[1] - dist)]
        
        edges.update({(c[0],c[2]), (c[2],c[1]), (c[1],c[3]), (c[3],c[0])})

    edges = list(edges)
    intersections = set()
    
    for i in range(len(edges)):
        for j in range(i+1, len(edges)):
            intersections.add(findIntersection(edges[i][0][0], edges[i][0][1],
                                               edges[i][1][0], edges[i][1][1],
                                               edges[j][0][0], edges[j][0][1],
                                               edges[j][1][0], edges[j][1][1]))

    intersections.remove(-1)
    intersections = {p for p in intersections if in_bounds(p,bound)}
    possible = set()
    
    for p in intersections:
        for n in [(1,0), (0,1), (-1,0), (0,-1)]:
            p2 = (p[0] + n[0], p[1] + n[1])
            if (
               (p2[0] + 1, p2[1]) in intersections and (p2[0], p2[1] + 1) in intersections and
               (p2[0] - 1, p2[1]) in intersections and (p2[0], p2[1] - 1) in intersections):
                possible.add(p2)

    for p in possible:
        detected = False
        for s in sensors:
            if manhattan(p[0],p[1],s[0],s[1]) <= sensors[s]:
                detected = True
                break
        if not detected:
            print(p[0] * 4000000 + p[1])
            break

def in_bounds(p, bound):
    return 0 <= p[0] <= bound and 0 <= p[1] <= bound

def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
    try:
        px= ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
        py= ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
        return (int(px), int(py))
    except ZeroDivisionError:
        return -1
        

def manhattan(x1, y1, x2, y2):return abs(x1-x2) + abs(y1-y2)
    
part1()
part2()