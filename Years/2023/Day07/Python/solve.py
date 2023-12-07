from functools import total_ordering 
    
@total_ordering
class Hand:
    def __init__(self, hand, value, wild = False):
        self.hand = hand
        self.value = value
        self.wild = wild

    def __eq__(self, other):
        return self.hand == other.hand
    
    def __lt__(self, other):
        values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, 
                  "T":10, "J":11, "Q":12, "K":13, "A":14 }
        
        if self.wild:
            values["J"] = 1
        
        if self.wild: 
            if self.wild_rank_hand() == other.wild_rank_hand():
                for i in range(len(self.hand)):
                    if values[self.hand[i]] < values[other.hand[i]]:
                        return True
                    if values[self.hand[i]] > values[other.hand[i]]:
                        return False
                    
            return self.wild_rank_hand() < other.wild_rank_hand()
        
        else: 
            if self.rank_hand() == other.rank_hand():
                for i in range(len(self.hand)):
                    if values[self.hand[i]] < values[other.hand[i]]:
                        return True
                    if values[self.hand[i]] > values[other.hand[i]]:
                        return False
                    
            return self.rank_hand() < other.rank_hand()
    
    def wild_rank_hand(self):
        max_hand_val = 0
        og_hand = self.hand
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K"]
        for value in values:
            self.hand = self.hand.replace("J", value)
            max_hand_val = max(max_hand_val, self.rank_hand())
            self.hand = og_hand

        return max_hand_val

    def rank_hand(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
        hist = [self.hand.count(v) for v in values]
        hand_set = set(self.hand)

        if 5 in hist: return 7
        if 4 in hist: return 6
        if 3 in hist and 2 in hist: return 5
        if 3 in hist: return 4
        if 2 in hist and len(hand_set) == 3: return 3
        if 2 in hist: return 2
        return 1
        

input_files = ["input.txt", "test_input.txt"]

file = 0
with open(input_files[file], 'r') as f:
    lines =  [a.strip() for a in f.readlines()]

hands = [Hand(line.split()[0], int(line.split()[1])) for line in lines]

def part1():
    p1_hands = sorted(hands)
    scores = [hand.value * (v + 1) for (v, hand) in enumerate(p1_hands)]
    print(sum(scores))

def part2():
    for hand in hands:
        hand.wild = True
    part1()

part1()
part2()