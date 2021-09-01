import random


def display_board(board):
    print("\n" * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ""
    while marker != 'X' and marker != '0':
        marker = input("Player 1 choose 'X' or '0': ")
    player1 = marker
    if player1 == 'X':
        return 'X', '0'
    else:
        return '0', 'X'


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a poistion(1-9): "))
    return position


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def replay():
    choice = input("Play Again? Yes or No: ")
    return choice == 'Yes'


print("Welcome to Tic Tac Toe")

while True:
    # Play the game

    # Set everything up (Board, Who's first, Choose marker
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " Will go first")

    play_game = input("Ready to play? y or n: ")

    if play_game == "y":
        game_on = True
    else:
        game_on = False

    # Game Play

    while game_on:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # win check
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1  has won")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    gmae_on = False
                else:
                    turn = 'Player2'
        else:
            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # win check
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2  has won")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    gmae_on = False
                else:
                    turn = 'Player1'

    if not replay():
        break
