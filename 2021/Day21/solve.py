import re
import random

input_files = ["input.txt", "test_input.txt"]

with open(input_files[1], 'r') as f:
    data = [list(map(int, re.findall("\d+", x))) for x in f.readlines()]

class Die():
    def __init__(self) -> None:
        self.value = 1
        self.rolls = 0

    def get_value(self):
        output = self.value
        self.value += 1
        if self.value > 100:
            self.value = 1

        self.rolls += 1
        
        return output

    def get_rolls(self):
        return self.rolls

class Player():
    def __init__(self, label, starting_place) -> None:
        self.label = label
        self.place = starting_place
        self.score = 0

    def advance(self, value, max=10):
        self.place = self.place + value
        if self.place > max:
            self.place = self.place % max

            if self.place == 0:
                self.place = max

        self.score += self.place

        return self.score

    def get_score(self):
        return self.score

    def get_place(self):
        return self.place


def sim_game(data):
    die = Die()
    playing = True
    players = [Player(x[0], x[1]) for x in data]

    while playing:
        for player in players:
            rolls = [die.get_value() for _ in range(3)]
            score = player.advance(sum(rolls))

            if score >= 1000:
                playing = False
                break

    players_ranked = sorted(players, key=lambda x: x.get_score())

    return players_ranked, die

def sim_rolls(cur_state, player):
    """
    input: ((p1_place, p1_score), (p2_place, p2_score))
    output: 3 new states representing rolling a 1, 2, or 3 for player
    """

    output = []

    for roll, ways in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
        new_place = cur_state[player][0] + roll + 1
        if new_place > 10:
            new_place = new_place % 10
        
        if player == 0:
            output.append(((new_place, cur_state[0][1] + roll + 1), 
                           (cur_state[1][0], cur_state[1][1]), ways))

        else:
            output.append(((cur_state[0][0], cur_state[0][1]), 
                           (new_place, cur_state[1][1] + roll + 1), ways))

    return output

def part1(data):
    players_ranked, die = sim_game(data)

    print(players_ranked[0].get_score() * die.get_rolls())

def part2(data):
    games = {}
    wins = [0,0]
    player = 0
    win_threshold = 21

    start = ((data[0][1], 0), (data[1][1], 0))
    games[start] = 1

    

part1(data)
test_input = ((9,0), (10,0))
part2(data)