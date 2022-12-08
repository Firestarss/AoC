import copy

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

def part1():
    read = False
    cur_dir = []
    files = {}

    for line in lines:
        if line.startswith("$"):
            if line.split(" ")[1] == "cd":
                if line.split(" ")[2] != "..": cur_dir.append(line.split(" ")[2])
                else: cur_dir.pop()
        else:
            if line.split(" ")[0].isdigit():
                record = int(line.split(" ")[0])
            else:
                record = "|".join(cur_dir) + "|" + line.split(" ")[1]

            if "|".join(cur_dir) in files: files["|".join(cur_dir)].append(record)
            else: files["|".join(cur_dir)] = [record]

    total = 0
    for file in files:
        if get_size(file, files) <= 100000: total += get_size(file, files)

    print(total)

    root_size = get_size("/", files)
    unused = 70000000 - root_size
    sizes = [get_size(x, files) for x in files]
    sizes.sort()

    for size in sizes:
        if size + unused > 30000000:
            print(size)
            break


def get_size(file_name, files):

    if all([isinstance(x, int) for x in files[file_name]]):
        return sum(files[file_name])

    else:
        r_sum = 0
        for item in files[file_name]:
            if isinstance(item, int): r_sum += item
            else: r_sum += get_size(item, files)

        return r_sum


part1()