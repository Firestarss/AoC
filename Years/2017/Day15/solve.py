gens = {"A": 783, "B": 325}
a = 16807
b = 48271

div = 2147483647


def solve():
    count = 0
    count2 = 0

    anums = []
    bnums = []
    for _ in range(40000000):
        gens["A"] = (gens["A"] * a) % div
        gens["B"] = (gens["B"] * b) % div

        if gens["A"] & 0xFFFF == gens["B"] & 0xFFFF:
            count += 1

        if min(len(anums), len(bnums)) > 5000000:
            continue

        if (gens["A"]) % 4 == 0:
            anums.append(gens["A"])

        if (gens["B"]) % 8 == 0:
            bnums.append(gens["B"])


    for i in range(5000000):
        if anums[i] & 0xFFFF == bnums[i] & 0xFFFF:
            count2 += 1

    print(count)
    print(count2)


solve()