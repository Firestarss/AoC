class Spell:
    def __init__(self, cost, dmg=0, heal=0, timer=0, effect=0):
        self.cost = cost
        self.dmg = dmg
        self.heal = heal
        self.timer = timer
        self.effect = effect

    def cast(self, state):
        player, boss, effects, total_mana = state

        # Check player can cast spell
        if player[1] < self.cost:
            return state

        # Check if spell is an effect
        if self.effect > 0:
            # Skip spell cast if effect is already active
            if effects[self.effect - 1] > 0:
                return state

            # Set timer if the effect is not active
            else:
                effects = list(effects)
                effects[self.effect - 1] = self.timer
                effects = tuple(effects)

        player = (player[0] + self.heal, player[1] - self.cost)
        boss = (boss[0] - self.dmg, boss[1])
        total_mana = total_mana + self.cost

        return (player, boss, effects, total_mana)         

def proc_effects(state):
    player, boss, effects, total_mana = state
    out_effects = tuple([max(0, x - 1) for x in effects])
    
    if effects[1] > 0:
        boss = (boss[0] - 3, boss[1])
    
    if effects[2] > 0:
        player = (player[0], player[1] + 101)

    return (player, boss, out_effects, total_mana)

def boss_turn(state):
    player, boss, effects, total_mana = proc_effects(state)

    if effects[0] > 0:
        health = player[0] - max(1, boss[1] - 7)
        player = (health, player[1])
    else:
        player = (player[0] - boss[1], player[1])

    return (player, boss, effects, total_mana)

def sim(boss_stats, hard):
    spells = (
        Spell(53, dmg = 4),                 # Magic Missile
        Spell(73, dmg = 2, heal = 2),       # Drain
        Spell(113, timer = 6, effect = 1),  # Shield
        Spell(173, timer = 6, effect = 2),  # Poison
        Spell(229, timer = 5, effect = 3))  # Recharge

    burn = Spell(0, heal = -1) # Spell used only in hard mode. Constant debuff on the player

    player = (50, 500)  # health, mana
    boss = boss_stats   # health, damage
    effects = (0, 0, 0) # shield, poison, recharge
    total_mana = 0

    start = (player, boss, effects, total_mana)

    stack = [start]
    v = set(start)
    min_mana = 9e50

    while stack:
        cur = stack.pop()

        # Start Player turn
        cur = proc_effects(cur)

        if hard:
            cur = burn.cast(cur)
            if cur[0][0] <= 0:
                continue

        for spell in spells:
            next = spell.cast(cur)
            if next == cur:
                continue
            next = boss_turn(next)

            # print_state(next)

            if next[1][0] <= 0:
                min_mana = min(min_mana, next[3])
                continue

            # if player isn't dead and total_mana isn't >= min_mana
            if next not in v and next[0][0] > 0 and next[3] < min_mana:
                v.add(next)
                stack.append(next)

    print(min_mana)


boss_stats = (58, 9) # input. [hit points, damage]

sim(boss_stats, False)
sim(boss_stats, True)