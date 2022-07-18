

input_files = ["input.txt", "test_input.txt"]

file = 1
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

