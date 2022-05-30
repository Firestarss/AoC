input = 864801
last_digit = input % 10
input_str = str(input)

def solve():
    recipies =  [3, 7]
    elf_pos = [0,1]
    p1_ans = 0
    p2_ans = 0
    while not p1_ans or not p2_ans:
        to_add = list(map(int, list(str(recipies[elf_pos[0]] + recipies[elf_pos[1]]))))
        recipies += to_add
        elf_pos[0] = (elf_pos[0] + recipies[elf_pos[0]] + 1) % len(recipies)
        elf_pos[1] = (elf_pos[1] + recipies[elf_pos[1]] + 1) % len(recipies)

        if len(recipies) > input + 10 and not p1_ans:
            p1_ans = "".join(list(map(str, recipies[input:input+10])))

        if last_digit in recipies[-2:] and len(recipies) > len(input_str) + 2 and not p2_ans:
            search_space = "".join(list(map(str, recipies[-len(input_str) - 2:])))
            if input_str in search_space:
                p2_ans = len(recipies) - len(input_str) - 2 + search_space.find(input_str)

    print(p1_ans)
    print(p2_ans)

solve()