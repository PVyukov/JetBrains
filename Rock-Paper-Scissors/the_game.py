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


def get_losers_set(option, options):
    index_mid = len(options) // 2
    index_option = options.index(option)
    head = ()
    if index_option < index_mid:
        tail = options[index_option + 1:index_option + index_mid + 1]
    else:
        tail = options[index_option + 1:]
        head = options[:index_mid - len(tail)]
    return set(tail + head)


options = ('gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
           'dragon', 'devil', 'lightning')
def_options = ('scissors', 'paper', 'rock')
file = 'rating.txt'
name = input('Enter your name: ')
print(f'Hello, {name}')
rating = get_rating(name, file)
user_option = input().split(',')
if len(user_option) < 3:
    user_option = def_options  # it's better to use 'options' variable as default one
print('Okay, let\'s start')
while True:
    user_input = input()
    # check input
    if user_input == '!exit':
        print('Bue')
        break
    elif user_input == '!rating':
        print(f'Your rating: {rating}')
        continue
    elif user_input not in options:
        print('Invalid input')
        continue
    # game logic
    comp_choice = random.choice(user_option)
    losers = get_losers_set(user_input, options)
    if user_input == comp_choice:
        rating += 50
        print(f'There is a draw ({comp_choice})')
    elif comp_choice in losers:
        rating += 100
        print(f'Well done. The computer chose {comp_choice} and failed')
    else:
        print(f'Sorry, but the computer chose {comp_choice}')
