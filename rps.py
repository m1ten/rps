# rock, paper, scissors game

import random

game_rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock',
}

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def main():
    print('Welcome to Rock, Paper, Scissors!')
    print('---------------------------------')
    print('Enter your choice: ')
    player1 = input('> ').lower()
    player2 = computer_choice()
    print('Player 2 chose: ' + player2)
    try:
        if game_rules[player1] == player2:
            print('Player 1 wins!')
        elif game_rules[player2] == player1:
            print('Player 2 wins!')
        else:
            print('It\'s a tie!')
    except ValueError:
        print('Invalid input')

if __name__ == '__main__':
    main()
