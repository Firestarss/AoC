import itertools

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    input_s = f.read()
    sections = input_s.split("\n\n")
    in_rules = sections[0].split("\n")
    updates = [list(map(int, x.split(","))) for x in sections[1].split("\n")]

    rules = dict()
    for rule in in_rules:
        value, key = list(map(int, rule.split("|")))
        if key in rules:
            rules[key].append(value)
        else:
            rules[key] = [value]

def is_valid(rules, update):
    seen = set()
    for page in update:
        seen.add(page)
        if page not in rules:
            continue
        for rule in rules[page]:
            if rule in update:
                if rule not in seen:
                    return False
    
    return True

def shuffle_valid(rules, update):
    perms = itertools.permutations(update)
    for perm in perms:
        if is_valid(rules, perm):
            return perm
        
    return None

def part1():
    output = 0

    for update in updates:
        if is_valid(rules, update):
            output += update[(len(update) - 1) // 2]

    print(output)

def part2():
    incorrect = [update for update in updates if not is_valid(rules, update)]
    valid = [shuffle_valid(rules, update) for update in incorrect]
    print(sum([update[(len(update) - 1) // 2] for update in valid]))

part1()
part2()