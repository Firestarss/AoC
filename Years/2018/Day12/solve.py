input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip().split("\n")

start_state = input[0][input[0].index(": ") + 2:].replace(".", "0").replace("#", "1")
start_state = {x for x in range(len(start_state)) if start_state[x] == "1"}
input = [x.replace(".", "0").replace("#", "1") for x in input[2:]]
rules = {x.split(" => ")[0]:x.split(" => ")[1] for x in input}

def set_to_string(state):
    out = ["#" if x in state else "." for x in range(min(state)-4, max(state) + 5)]
    return "".join(out)

def step(state):
    state_to_add = set()
    state_to_remove = set()

    seen = set()

    for cur in state:
        for i in range(cur-2, cur+3):
            if i in seen: continue

            key = "".join(["1" if x in state else "0" for x in range(i-2,i+3)])
            if key in rules:
                seen.add(i)
                if rules[key] == "1":
                    state_to_add.add(i)
                if rules[key] == "0":
                    state_to_remove.add(i)

            else:
                state_to_remove.add(i)

    state = state.difference(state_to_remove)
    state = state.union(state_to_add)

    return state

def part1(state):
    for i in range(20):
        state = step(state)

    print(sum(state))

def part2(state):
    values = [sum(state)]
    for i in range(20001):
        state = step(state)
        values.append(sum(state))

    print(values[-1] + (50000000000 - 20000) * (values[-1] - values[-2]))

part1(start_state)
part2(start_state)
