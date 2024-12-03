input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [list(map(int,a.strip().split())) for a in f.readlines()]

def valid_level(level):
    if level not in [sorted(level), sorted(level)[::-1]]:
        return False
    for i in range(len(level) -1):
            dist = abs(level[i] - level[i+1])
            if dist < 1 or dist > 3:
                return False
                
    return True

def all_levels(level):
    if valid_level(level): return True
    for i in range(len(level)):
        if valid_level(level[:i] + level[i+1:]):
            return True
        
    return False

def part1():
    print(sum([valid_level(level) for level in lines]))

def part2():
    print(sum([all_levels(level) for level in lines]))


part1()
part2()