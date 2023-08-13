input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    line =  f.read().strip()

def solve(window = 4):
    for i in range(len(line)):
        if len(set(line[i:i + window])) == window:
            print(i+window)
            break

solve()
solve(14)