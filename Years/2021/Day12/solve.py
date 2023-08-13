import json

input_file = ["input.txt", "test_input.txt"]

data = []
graph = {}
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip().split("-")
        data.append(temp)

        for node in temp:
            if node not in graph:
                graph[node] = []

        if temp[1] != "start":
            graph[temp[0]].append(temp[1])

        if temp[0] != "start":
            graph[temp[1]].append(temp[0])


def find_all_paths(visited = ["start"]):
    cur = visited[-1]
    if cur == "end":
        return [visited]

    new_paths = []
    for adj in graph[cur]:
        if not (adj.islower() and adj in visited):
            new_paths += find_all_paths(visited + [adj])
    return new_paths


def find_all_paths2(visited = ["start"], explored_little = False):
    cur = visited[-1]
    if cur == "end":
        return [visited]

    new_paths = []

    for adj in graph[cur]:
        if adj.islower() and adj in visited:
            if not explored_little:
                new_paths += find_all_paths2(visited + [adj], True)
        else:
            new_paths += find_all_paths2(visited + [adj], explored_little)
    return new_paths


print(len(find_all_paths()))
print(len(find_all_paths2()))