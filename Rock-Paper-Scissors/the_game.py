import random

user = input()
options = ('rock', 'paper', 'scissors')
comp = random.choice(options)
winners = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
if user == comp:
    print(f'There is a draw ({comp})')
elif winners[user] == comp:
    print(f'Sorry, but the computer chose {comp}')
else:
    print(f'Well done. The computer chose {comp} and failed')