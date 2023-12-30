input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  f.read().strip().split(",")

def HASH(string):
    cur = 0
    for c in string:
        cur += int(ord(c))
        cur *= 17
        cur %= 256

    return cur

def part1():
    print(sum([HASH(x) for x in lines]))

def part2():
    boxes = {i:[] for i in range(256)}
    for line in lines:
        if line[-1] == "-":
            label = line[:-1]
            box = HASH(label)

            for i, lens in enumerate(boxes[box]):
                if lens[0] == label:
                    boxes[box].pop(i)
                    break


        else:
            line = line.split("=")
            label = line[0]
            focal_length = int(line[1])
            box = HASH(label)

            replaced = False

            for i, lens in enumerate(boxes[box]):
                if lens[0] == label:
                    boxes[box][i] = (label, focal_length)
                    replaced = True
                    break

            if not replaced:
                boxes[box].append((label, focal_length))

    total = []
    for box in boxes:
        for i, lens in enumerate(boxes[box]):
            box_num = box + 1
            slot_num = i + 1
            focal_length = lens[1]
            total.append(box_num * slot_num * focal_length)

    print(sum(total))

part1()
part2()