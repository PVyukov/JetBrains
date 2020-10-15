import random


def get_rating(name, file):
    f = open(file, 'r', encoding='utf-8')
    for i in f:
        n, r = i.split()
        if n == name:
            return int(r)
    else:
        return 0
    f.close


file = 'rating.txt'
name = input('Enter your name: ')
print(f'Hello, {name}')
rating = get_rating(name, file)
while True:
    user = input()
    options = ('rock', 'paper', 'scissors')
    # check input
    if user == '!exit':
        print('Bue')
        break
    elif user == '!rating':
        print(f'Your rating: {rating}')
        continue
    elif user not in options:
        print('Invalid input')
        continue
    # game logic
    comp = random.choice(options)
    winners = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    if user == comp:
        rating += 50
        print(f'There is a draw ({comp})')
    elif winners[user] == comp:
        print(f'Sorry, but the computer chose {comp}')
    else:
        rating += 100
        print(f'Well done. The computer chose {comp} and failed')
