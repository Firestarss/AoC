

input_file = ["input.txt", "test_input.txt"]

data = []
with open(input_file[1], "r") as file:
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

scores = []

for point in data:

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

    if not done:
        score = 0
        score_values = {")":1,"]":2,"}":3,">":4}
        for c in expect[::-1]:
            score *= 5
            score += score_values[c]
        scores.append(score)

scores = sorted(scores)
print(scores[len(scores)//2] == 4330777059)