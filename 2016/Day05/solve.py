import hashlib
import random
import string

input = "ugkcyxxp"
hex_digits = string.hexdigits[:16]

def solve():
    m = hashlib.md5(input.encode('utf-8'))
    p1 = list()
    p2 = ["", "", "", "", "", "", "", ""]
    i = 0

    print()
    while len("".join(p2)) < 8:
        m_copy = m.copy()
        m_copy.update(str(i).encode('utf-8'))
        hash = m_copy.hexdigest()
        if hash[:5] == "0" * 5:
            p1.append(hash[5])

            if hash[5].isdigit() and int(hash[5]) < 8 and p2[int(hash[5])] == "":
                p2[int(hash[5])] = hash[6]

        i += 1

        if i % 100000 == 0:
            display(p1, p2)

    display(p1, p2, False)

def display(p1, p2, reset = True):
    p1 = "".join(p1)[:8]

    for i in range(8):
        if i < len(p1):
            print('\033[92m' + p1[i] + '\033[0m', end="")
        else:
            print('\033[91m' + random.choice(hex_digits) + '\033[0m', end="")
    print("\n", end="")

    for char in p2:
        if char == "":
            print('\033[91m' + random.choice(hex_digits) + '\033[0m', end="")
        else:
            print('\033[92m' + char + '\033[0m', end="")

    if reset:
        print("\033[F", end = "")
    else:
        print("\n")

solve()