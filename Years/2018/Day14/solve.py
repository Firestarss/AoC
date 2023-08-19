input_str = "077201"
input_num = int(input_str)
last_digit = input_num % 10

def solve():
    recipes =  [3, 7]
    elf_pos = [0,1]
    p1_ans = 0
    p2_ans = 0
    while not p1_ans or not p2_ans:
        to_add = list(map(int, list(str(recipes[elf_pos[0]] + recipes[elf_pos[1]]))))
        recipes += to_add
        elf_pos[0] = (elf_pos[0] + recipes[elf_pos[0]] + 1) % len(recipes)
        elf_pos[1] = (elf_pos[1] + recipes[elf_pos[1]] + 1) % len(recipes)

        if len(recipes) > input_num + 10 and not p1_ans:
            p1_ans = "".join(list(map(str, recipes[input_num:input_num+10])))

        if last_digit in recipes[-2:] and len(recipes) > len(input_str) + 2 and not p2_ans:
            search_space = "".join(list(map(str, recipes[-len(input_str) - 2:])))
            if input_str in search_space:
                p2_ans = len(recipes) - len(input_str) - 2 + search_space.find(input_str)

    print(p1_ans)
    print(p2_ans)

solve()
