import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def part1():
    start = int(lines[0])
    current_time = start
    times = list(map(int, re.findall("\d+", lines[1])))

    while True:
        for time in times:
            if current_time % time == 0:
                print(time * (current_time - start))
                return
        current_time += 1

def part2():
    schedule = [(i, int(bus_id)) for i, bus_id in enumerate(lines[1].split(',')) if bus_id != 'x']
    jump = schedule[0][1]
    time_stamp = 0
    for delta, bus_id in schedule[1:]:
        while (time_stamp + delta) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    print(time_stamp)

part1()
part2()