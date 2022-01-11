

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[0], "r") as file:
    for line in file:
        temp = line.strip()
        data.append(temp)

def inverse(c):
    if c == "(":
        return ")"

    if c == "[":
        return "]"

    if c == "{":
        return "}"

    if c == "<":
        return ">"


track = {")":0,"]":0,"}":0,">":0}

for point in data:
    local_track = {"(":0,"[":0,"{":0,"<":0}

    done = False
    expect = ""
    for c in point:
        if done:
            break
        if c in "([{<":
            expect += inverse(c)
        else:
            if c == expect[-1]:
                expect = expect[:-1]
            else:
                done = True
                track[c] += 1


print((track[")"]*3) + (track["]"]*57) + (track["}"]*1197) + (track[">"]*25137))