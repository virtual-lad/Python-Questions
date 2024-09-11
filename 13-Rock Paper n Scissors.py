'''
Rock, Paper, and Scissor
'''

a = input('Enter your choice: ')
b = ['rock','paper','scissors']

import random

c = random.choice(b)

print('I chose: ', c)

if a == 'rock' and c == 'paper':
    print('Computer won!')
elif a == 'rock' and c == 'scissors':
    print('You won!')
elif a == 'paper' and c == 'rock':
    print('You won!')
elif a == 'paper' and c == 'scissors':
    print('Computer won!')
elif a == 'scissors' and c == 'rock':
    print('Computer won!')
elif a == 'scissors' and c == 'paper':
    print('You won!')
else:
    print('TIE')

# THE END