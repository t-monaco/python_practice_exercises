import time
import random
import os
import pyinputplus as pyip


# ------- START GAME / SELECT PLAYER -------#

def start_game():
    print('***** WELCOME *****')
    time.sleep(1)
    while True:
        player = input('Select player: X or O\n').upper()
        if player == 'X':
            human = '\033[92mX\033[00m'
            computer = '\033[91mO\033[00m'
            break
        elif player == 'O':
            human = '\033[92mO\033[00m'
            computer = '\033[91mX\033[00m'
            break
        else:
            print('Please select one of the two posibilities. ("X" 0r "O")')
    return human, computer


# ------- CREATE BOARD -------#


def board():
    print('TIC TAC TOE\n')
    print('       |       |       ')
    print(' 1  {}  | 2  {}  | 3  {}  '.format(matrix[0], matrix[1], matrix[2]))
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print(' 4  {}  | 5  {}  | 6  {}  '.format(matrix[3], matrix[4], matrix[5]))
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print(' 7  {}  | 8  {}  | 9  {}  '.format(matrix[6], matrix[7], matrix[8]))
    print('       |       |       ')

    return True


# ------- GAME RESULTS -------#


def tie(matrix):
    tie = True
    i = 0
    while (tie == True and i < 9):
        if matrix[i] == ' ':
            tie = False
        i += 1
    return tie


def victory(matrix):
    if matrix[0] == matrix[1] == matrix[2] != ' ' \
            or matrix[3] == matrix[4] == matrix[5] != ' ' \
            or matrix[6] == matrix[7] == matrix[8] != ' ' \
            or matrix[0] == matrix[3] == matrix[6] != ' ' \
            or matrix[1] == matrix[4] == matrix[7] != ' ' \
            or matrix[2] == matrix[5] == matrix[8] != ' ' \
            or matrix[0] == matrix[4] == matrix[8] != ' ' \
            or matrix[2] == matrix[4] == matrix[6] != ' ':
        return True
    else:
        return False


# ------- MOVEMENTS -------#


def human_move():
    while True:
        # box = int(input("Select a box: "))
        box = pyip.inputNum('Select a box:', min=1, max=9)
        if box not in range(1, 10):
            print('Box not available')
        else:
            if matrix[box - 1] == ' ':
                matrix[box - 1] = human
                break
            else:
                print('Box not available')


def computer_move():
    box = 9
    stop = False
    # for i in range(0, 9):
    #     copy = list(matrix)
    #     print(copy)
    #     if copy[i] == ' ':
    #         copy[i] = computer
    #         if victory(copy):
    #             box = i
    #
    # if box == 9:
    #     for j in range(0, 9):
    #         copy = list(matrix)
    #         if copy[j] == ' ':
    #             copy[j] = human
    #             if victory(copy):
    #                 box = j

    # if box == 9:
    #     while not stop:
    #         box = random.randint(0, 8)
    #         if matrix[box] == ' ':
    #             return True

    for i in range(0, 9):
        matrix_replica = list(matrix)
        if matrix_replica[i] == ' ':
            matrix_replica[i] = computer
            if victory(matrix_replica):
                box = i
                stop = True

    if box == 9:
        for j in range(0, 9):
            matrix_replica = list(matrix)
            if matrix_replica[j] == ' ':
                matrix_replica[j] = human
                if victory(matrix_replica):
                    box = j
                    stop = True

    while not stop:
        box = random.randint(0, 8)
        if matrix[box] == ' ':
            break

    matrix[box] = computer


# ------- GAME DEVELOPMENT -------#
while True:
    matrix = [' '] * 9
    os.system('clear')  # CLEAR SCREEN BEFORE GAME STARTS
    human, computer = start_game()
    game = True
    winner = 0

    while game:
        winner += 1
        os.system('clear')
        board()

        if victory(matrix):
            if winner % 2 == 0:
                print('*****PLAYER WINS*****')
                print('*****END GAME*****')
                print('*****\n RESTARTING*****')
                time.sleep(5)
                game = False
            else:
                print('*****COMPUTER WINS*****')
                print('*****END GAME*****')
                print('*****\n RESTARTING*****')
                time.sleep(5)
                game = False
        elif tie(matrix):
            print('*****DRAW*****')
            print('*****END GAME*****')
            print('*****\n RESTARTING*****')
            time.sleep(5)
            game = False
        elif winner % 2 == 0:
            print('Computer processing')
            time.sleep(2)
            computer_move()
        else:
            human_move()
