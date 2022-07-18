import re

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    passports =  [a.strip().replace("\n", " ") for a in f.read().split("\n\n")]

def validate_data(data):
    valid = True

    for field in data:
        cur = field.split(":")

        if cur[0] == "byr":
            if not (1920 <= int(cur[1]) <= 2002): valid = False
        if cur[0] == "iyr":
            if not (2010 <= int(cur[1]) <= 2020): valid = False
        if cur[0] == "eyr":
            if not (2020 <= int(cur[1]) <= 2030): valid = False
        if cur[0] == "hgt":
            unit = cur[1][-2:]
            height = int(re.findall("\d+", cur[1])[0])

            if unit not in ["in", "cm"]: valid = False
            if unit == "cm" and not (150 <= height <= 193): valid = False
            if unit == "in" and not (59 <= height <= 76): valid = False
        if cur[0] == "hcl":
            if len(cur[1]) != 7: valid = False
            if not re.search("#[0-9a-zA-Z]{6}", cur[1]): valid = False
        if cur[0] == "ecl":
            if cur[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: valid = False
        if cur[0] == "pid":
            if len(cur[1]) != 9: valid = False
            if not re.search("\d{9}", cur[1]): valid = False

    return valid


def solve():
    num_valid = 0
    data_valid = 0
    for passport in passports:
        valid = True
        for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if field not in passport:
                valid = False

        if valid:
            num_valid += 1

            data = passport.split(" ")

            if validate_data(data):
                data_valid += 1

    print(num_valid)
    print(data_valid)

solve()