class human:
    name = ''
    health = 100
    mood = 100
    money = 100
    def __init__(self, name='Петя', health=100, mood=100, money=100):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money
        def __str__(self):
            return f' - {self.name} -\n' \
                   f' health: {self.health}\n' \
                   f' mood: {self.mood}\n' \
                   f' money: {self.money}'
def alive(self):
 self.health > 0
def alive(self):
 self.mood > 0
def alive(self):
 self.money > 0
player1 = human("Петя", health=100)
player1.health = 0

