import random


# Write your code here
def replace_char(char_in, word, new_word):
    new_word = list(new_word)
    word = list(word)
    if len(new_word) != len(word):
        raise
    else:
        for i, c in enumerate(word):
            if c == char_in:
                new_word[i] = c
    return ''.join(new_word)

# The second var
# def replace_char(char_in, word, new_word):
#     a = [word[j] if new_word[j] == '-' and word[j] == char_in else new_word[j] for j in range(len(word))]
#     return ''.join(a)


choic_def = ['python', 'java', 'kotlin', 'javascript']
rand_ch = random.choice(choic_def)
# rand_ch = 'kotlin'
print("H A N G M A N")
tries = 8
show_word = '-' * len(rand_ch)
guested_letters = []
menu = None
while not (menu == 'play' or menu == 'exit'):
    menu = input('Type "play" to play the game, "exit" to quit: ')
if menu == 'play':
    while tries > 0:
        print('\n' + show_word)
        if '-' not in show_word:
            print('You guessed the word!')
            print('You survived!')
            break
        letter = input('Input a letter:')
        if len(letter) != 1:
            print('You should input a single letter')
        elif letter in guested_letters:
            print('You already typed this letter')
        elif not letter.islower():
            print('It is not an ASCII lowercase letter')
        elif letter in rand_ch:
            show_word = replace_char(letter, rand_ch, show_word)
        else:
            print('No such letter in the word')
            tries -= 1
        guested_letters.append(letter)
    else:
        print('You lost!')


