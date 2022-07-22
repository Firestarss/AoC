input = [9,19,1,6,0,5,4]

def solve(num):
    i = len(input)
    places = {v:[i] for i, v in enumerate(input)}
    last = input[-1]
    
    while i < num:
        if len(places[last]) == 1:
            last = 0
            places[0].append(i)
        else:
            new = places[last][-1] - places[last][-2]
            last = new
            if new in places:
                places[new].append(i)
            else:
                places[new] = [i]

        i += 1

    print(last)

solve(2020)
solve(30000000)