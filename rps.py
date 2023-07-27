import random

game_rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock',
}

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def main(player1, player2, user_score, computer_score):
    print(f'Player 2 chose: {player2}')
    try:
        if game_rules[player1] == player2:
            user_score += 1
            print('Player 1 wins!')
        elif game_rules[player2] == player1:
            computer_score += 1
            print('Player 2 wins!')
        else:
            print('It\'s a tie!')
    except KeyError:
        print('Invalid input')
    return user_score, computer_score

if __name__ == '__main__':
    user_score = 0
    computer_score = 0
    print('Welcome to Rock, Paper, Scissors!')
    print('---------------------------------')

    # play the game or simulate it
    action = input('Play or Simulate? ').lower()
            
    rounds = 0
    while rounds <= 0:
        try:
            rounds = int(input('Number of rounds to play: '))
        except ValueError:
            pass
        
    for i in range(int(rounds)):
        print(f'Round {i + 1}')
        if action == 'simulate' or action == 'sim':
            player1 = computer_choice()
            player2 = computer_choice()
        else:
            print('Enter your choice: ')
            player1 = input('> ').lower()
            player2 = computer_choice()            
        
        user_score, computer_score = main(player1, player2, user_score, computer_score)
        
    print(f'Final Score: Player 1 - {user_score}, Player 2 - {computer_score}')