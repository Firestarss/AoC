

input_files = ["input.txt", "test_input.txt"]

with open(input_files[1], 'r') as f:
    data =  [a.strip() for a in f.readlines()]
