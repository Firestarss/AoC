import numpy as np

input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

input = [[x[:18], x[19:]] for x in input]
input.sort()

def sovle():
    schedule = {}
    cur_guard = -1

    for i in range(len(input)):
        cur = input[i]

        if cur[1].startswith("Guard"):
            guard_num = int(cur[1].split(" ")[1][1:])
            cur_guard = guard_num

            if guard_num not in schedule:
                schedule[guard_num] = np.zeros(60, dtype=int)

        if cur[1].startswith("falls"):
            next = input[i + 1]

            cur_time = int(cur[0][-3:-1])
            next_time = min(59, int(next[0][-3:-1]))

            schedule[cur_guard][cur_time:next_time] += 1

    max_time = 0
    guard = -1
    for key in schedule:
        if sum(schedule[key]) > max_time:
            guard = key
            max_time = sum(schedule[key])

    print(guard * np.where(schedule[guard] == max(schedule[guard]))[0][0])

    max_time = 0
    guard = -1
    for key in schedule:
        if max(schedule[key]) > max_time:
            guard = key
            max_time = max(schedule[key])

    print(guard * np.where(schedule[guard] == max_time)[0][0])

sovle()