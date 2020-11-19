from random import randint, choice
import sys

print('ROCK, PAPER, SCISSORS')

# * THIS VARIABLES KEEP TRACK OF THE GAME RESULTS
wins = 0
losses = 0
ties = 0

try:
    while True:  # * The main loop
        print(f'\n{wins} Wins, {losses} Losses, {ties} Ties')
        game_choices = ['r', 'p', 's']

        while True:  # * Player input loop
            player_move = input('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit: ')
            if player_move == 'q':
                print('\nGood game BRO')
                print(f'{wins} Wins, {losses} Losses, {ties} Ties')
                sys.exit()

            if player_move in game_choices:
                break  # * Break the player loop

            print('\nPlease type r, p, s or q')

        # * Display player move
        if player_move == 'r':
            print('\nROCK vesus...')
        elif player_move == 'p':
            print('\nPAPER vesus...')
        elif player_move == 's':
            print('\nSCISSORS vesus...')

        # * Display computer move
        # computer_move = game_choices[randint(0, 2)]
        computer_move = choice(game_choices)
        if computer_move == 'r':
            print('ROCK')
        elif computer_move == 'p':
            print('PAPER')
        elif computer_move == 's':
            print('SCISSORS')

        # * Display and record results
        if player_move == computer_move:
            print('\nIt is a tie')
            ties += 1
        elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or (player_move == 's' and computer_move == 'p'):
            print('\nYou win!')
            wins += 1
        elif (computer_move == 'r' and player_move == 's') or (computer_move == 'p' and player_move == 'r') or (computer_move == 's' and player_move == 'p'):
            print('\nYou Lose')
            losses += 1
except KeyboardInterrupt:
    print('\nGood game BRO')
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
