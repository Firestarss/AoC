class DLLNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        if prev: self.prev = prev
        if next: self.next = next

    def set_prev(self, value): self.prev = value
    def set_next(self, value): self.next = value
    def get_value(self): return self.value

    def get_next(self, i = 1):
        cur = self
        for _ in range(i): cur = cur.next
        return cur

    def get_prev(self, i = 1):
        cur = self
        for _ in range(i): cur = cur.prev
        return cur

    def relink(self, prev, next):
        self.set_prev(prev)
        self.set_next(next)

def solve(num_players, last_marble):
    cur = DLLNode(0)
    cur.relink(cur, cur)
    zero = cur
    players = [0 for _ in range(num_players)]

    for i in range(1, last_marble + 1):
        if i % 23 == 0:
            score = i
            cur = cur.get_prev(6)
            score += cur.get_value()
            
            cur.get_prev().set_next(cur.get_next())
            cur.get_next().set_prev(cur.get_prev())

            players[i % num_players - 1] += score

        else:
            cur = cur.get_next(2)
            new_node = DLLNode(i, cur, cur.get_next())

            relink = (cur, cur.get_next())
            relink[0].set_next(new_node)
            relink[1].set_prev(new_node)

    print(max(players))
    
num_players = 465
last_marble = 71498

solve(num_players, last_marble)
solve(num_players, last_marble * 100)
