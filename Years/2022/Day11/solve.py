input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.read().split("\n\n")]
    lines = [[b.strip() for b in a.split("\n")] for a in lines]

class Monkey:
    def __init__(self, starting_items, operation, test):
        self.items = list(map(int, starting_items.split(", ")))
        self.operation = operation.replace("old", "item")
        self.test = list(map(int, test))
        self.inspections = 0

    def act(self, divisor, div3 = True):
        output = []

        for _ in range(len(self.items)):
            item = self.items.pop(0)
            self.inspections += 1
            item = eval(self.operation)
            if div3: item = item // 3
            else: item %= divisor

            if item % self.test[0] == 0: output.append((self.test[1], item))
            else: output.append((self.test[2], item))

        return output
    
    def catch(self, v): self.items.append(v)

    def get_inspections(self): return self.inspections

    def __str__(self):
        return f"{self.items}\n{self.operation}\n{self.test}"

def solve(p1 = True, turns = 20):
    monkeys = []
    divisors = 1
    for line in lines:
        items = line[1].split(": ")[1]
        operation = line[2].split("= ")[1]
        test = [line[3].split(" ")[-1], line[4].split(" ")[-1], line[5].split(" ")[-1]]

        monkeys.append(Monkey(items, operation, test))

        divisors *= int(test[0])

    for i in range(turns):
        for monkey in monkeys:
            thrown = monkey.act(divisors, p1)
            for item in thrown:
                monkeys[item[0]].catch(item[1])

    inspections = sorted([monkey.get_inspections() for monkey in monkeys])[::-1]
    print(inspections[0] * inspections[1])

solve()
solve(False, 10000)