class Monster:
    def __init__(self, name, hp, mp, power, speed, critical, defense):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = hp
        self.max_mp = mp
        self.power = power
        self.speed = speed
        self.critical = critical
        self.defense = defense
