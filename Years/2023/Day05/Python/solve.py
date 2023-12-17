

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  f.read().strip().split("\n\n")

lines = [line.split("\n") for line in lines]

seeds = list(map(int, lines[0][0][7:].split()))

conversions = {}
maps = {}

reverse_stages = {}

for line in lines[1:]:
    key = line[0].split()[0].split("-to-")
    conversions[key[0]] = key[1]
    maps[key[0]] = [tuple(map(int, l.split())) for l in line[1:]]

for stage in conversions:
    reverse_stages[conversions[stage]] = stage

def part1(p=True):
    current_stage = "seed"
    p1_seeds = seeds[::]

    while current_stage != "location":
        p1_seeds = step(p1_seeds, current_stage)
        current_stage = conversions[current_stage]
    
    if p: print(min(p1_seeds))
    return min(p1_seeds)

def part2():
    test_num = 0

    p1_answer = part1(False)

    while True:
        if check_valid_seed(location_to_seed(test_num)):
            print(test_num)
            break
        test_num += 1


def step(seeds, stage):
    output = []
    for seed in seeds:
        value = seed
        for conversion in maps[stage]:
            if conversion[1] <= seed < (conversion[1] + conversion[2]):
                value = convert_range(
                    conversion[1], 
                    conversion[1] + conversion[2],
                    conversion[0],
                    conversion[0] + conversion[2],
                    seed)
                break

        output.append(value)
    return output

def check_valid_seed(seed):
    for i in range(0, len(seeds), 2):
        if seeds[i] <= seed < seeds[i] + seeds[i+1]:
            return True
    return False

def location_to_seed(seed):
    stage = "location"
    while stage != "seed":
        conv_stage = reverse_stages[stage]
        for conversion in maps[conv_stage]:
            if conversion[0] <= seed < (conversion[0] + conversion[2]):
                seed = convert_range(
                    conversion[0], 
                    conversion[0] + conversion[2],
                    conversion[1],
                    conversion[1] + conversion[2],
                    seed)
                break
        stage = reverse_stages[stage]

    return seed

def convert_range(OldMin, OldMax, NewMin, NewMax, OldValue):
    OldRange = (OldMax - OldMin)
    if (OldRange == 0):
        NewValue = NewMin
    else:
        NewRange = (NewMax - NewMin)  
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    return int(NewValue)

part1()
part2()