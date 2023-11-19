class job:
    name = ''
    health = 5
    mood = 20
    money = 100
    def __init__(self, name, health=5, mood=20, money=100):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

        def __str__(self):
            return f' - {self.name} -\n' \
                   f' health: {self.health}\n' \
                   f' mood: {self.mood}\n' \
                   f' money: {self.money}'
