import string


input_files = ["input.txt", "test_input.txt"]

file_num = 0
with open(input_files[file_num], 'r') as f:
    input = f.read().strip()

def reduce(input):
    polymer = input[:]
    pairs = set()
    for letter in string.ascii_lowercase:
        pairs.add(letter + letter.upper())
        pairs.add(letter.upper() + letter)
    
    while True:
        start = polymer[:]

        for pair in pairs:
            polymer = polymer.replace(pair, "")

        if polymer == start:
            return polymer

def part1():
    print(len(reduce(input)))

def part2():
    reduced_polymer = reduce(input)
    min_polymer = len(reduced_polymer)
    
    for letter in string.ascii_lowercase:
        temp_input = reduced_polymer.replace(letter, "").replace(letter.upper(), "")
        min_polymer = min(min_polymer, len(reduce(temp_input)))

    print(min_polymer)

part1()
part2()