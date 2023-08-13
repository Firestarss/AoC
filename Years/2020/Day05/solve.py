

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def solve():
    ids = [int(x.replace("L", "0").replace("R", "1").replace("F", "0").replace("B", "1"), 2) for x in lines]
    ids.sort()
    print(max(ids))
    
    for i in range(len(ids)):
        if ids[i+1] - ids[i] != 1:
            print(ids[i] + 1)
            break

solve()