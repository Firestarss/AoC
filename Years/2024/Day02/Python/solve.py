input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [list(map(int,a.strip().split())) for a in f.readlines()]

def valid_level(level):
    for i in range(len(level) -1):
            dist = abs(level[i] - level[i+1])
            if dist < 1 or dist > 3:
                return False
            if level[0] > level[1]:
                if level[i] < level[i+1]:
                    return False
            if level[0] < level[1]:
                if level[i] > level[i+1]:
                    return False
                
    return True

def all_levels(level):
    if valid_level(level): return True
    for i in range(len(level)):
        if valid_level(level[:i] + level[i+1:]):
            return True
        
    return False

def part1():
    count = len(lines)
    for level in lines:
        for i in range(len(level) -1):
            dist = abs(level[i] - level[i+1])
            if dist < 1 or dist > 3:
                count -= 1
                break
            if level[0] > level[1]:
                if level[i] < level[i+1]:
                    count -= 1
                    break
            if level[0] < level[1]:
                if level[i] > level[i+1]:
                    count -= 1
                    break

    print(count)

def part2():
    count = len(lines)
    for level in lines:
        if not all_levels(level):
            count -=1
    
    print(count)


part1()
part2()