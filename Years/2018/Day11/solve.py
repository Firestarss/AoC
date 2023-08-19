from itertools import product
input = 8199

def calc_power(coord):
    rack_id = coord[0] + 10
    return ((rack_id * coord[1]) + input) * rack_id // 100 % 10 - 5

def build_summed_area_table():
    table = {key:calc_power(key) for key in product(range(1, 301), repeat=2)}
    for coord in product(range(2, 301), repeat=2):
        x, y = coord
        table[coord] += table[(x, y-1)] + table[(x-1, y)] - table[(x-1, y-1)]
    return table

def largest_submatrix(m, s):
    r = range(1,301-s)
    return sorted([(m[(j,i)]+m[(j+s,i+s)]-m[(j+s,i)]-m[(j,i+s)], (j+1,i+1), s) for j in r for i in r])[-1]

table = build_summed_area_table()

def part1():
    coord = largest_submatrix(table, 3)[1]
    print(f"{coord[0]},{coord[1]}")

def part2():
    out = sorted(largest_submatrix(table, x) for x in range(2, 300))[-1]
    print(f"{out[1][0]},{out[1][1]},{out[-1]}")

part1()
part2()
