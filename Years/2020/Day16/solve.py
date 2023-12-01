import re
import math
with open("input.txt", "r") as infile:
    data = infile.read().strip().split("\n\n")

rules = data[0].split("\n")
my_ticket = list(map(int, data[1].split("\n")[1].split(",")))
other_tickets = data[2].split("\n")[1:]

labled_ranges = dict()
for rule in rules:
    key = rule[:rule.find(":")]
    value = [list(map(int, x)) for x in re.findall("(\d+)-(\d+)", rule)]
    value = set().union(*[set(range(x[0], x[1]+1)) for x in value])
    labled_ranges[key] = value

def is_valid_row(values, row, valid_tickets):
    valid = True
    for ticket in valid_tickets:
        if ticket[row] not in values:
            valid = False
            break
    return valid

def find_valid_rows(rule_name, valid_tickets):
    valid = []
    for row in range(len(labled_ranges)):
        if is_valid_row(labled_ranges[rule_name], row, valid_tickets):
            valid.append(row)

    return valid

def solve():
    invalid_vals = []
    valid_tickets = [my_ticket]
    valid = set().union(*labled_ranges.values())

    for ticket in other_tickets:
        ticket = list(map(int, ticket.strip().split(",")))
        valid_ticket = True
        for value in ticket:
            if value not in valid:
                invalid_vals.append(value)
                valid_ticket = False
        if valid_ticket: valid_tickets.append(ticket)

    print(sum(invalid_vals))

    possible_rows = {rule:find_valid_rows(rule, valid_tickets) for rule in labled_ranges}
    claimed_rows = set([possible_rows[x][0] for x in possible_rows if len(possible_rows[x]) == 1])

    while len(set([len(possible_rows[x]) for x in possible_rows])) != 1:
        for row in possible_rows:
            if len(possible_rows[row]) == 1: continue
            possible_rows[row] = list(set(possible_rows[row]).difference(claimed_rows))
            if len(possible_rows[row]) == 1: claimed_rows.add(possible_rows[row][0])

    print(math.prod([my_ticket[possible_rows[x][0]] for x in possible_rows if x.startswith("departure")]))

solve()
