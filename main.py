from human import human
from job import job
import random
player1 = human(name='Петя', health=100,mood=100, money=100)
player2 = job(name='работа', health=5,mood=20, money=100)
print(player1)
print(player2)
print(f'{player1.name} пошол на роботу  ')
print(f'{player1.health} - {player2.health} ')
print(f'У {player1.name} осталось {player1.health-player2.health} здоровья.')
print(f'{player1.mood} - {player2.mood} настроение')
print(f'У {player1.name} осталось {player1.mood-player2.mood} настроение.')
print(f'{player1.money} + {player2.money} ')
print(f' {player1.name} заработал {player1.money+player1.money} денег.')
for human in job:
    print(human, '\n')
    print(job, '\g')


