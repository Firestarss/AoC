filenames = ["input.txt", "test_input.txt"]
file_num = 0

with open(filenames[file_num], "r") as infile:
    input = infile.read().strip().split("\n")

input = [x.split(" a ") for x in input]

components = set()
start_state = [1]
for i in range(len(input)):
    temp = []
    for substring in input[i]:
        if "microchip" in substring:
            element = substring.split("-")[0]
            components.add(element + " m")
            temp.append(element + " m")

        elif "generator" in substring:
            element = substring.split(" ")[0]
            components.add(element + " g")
            temp.append(element + " g")

    start_state.append(tuple(temp))


print(components)
print(tuple(start_state))