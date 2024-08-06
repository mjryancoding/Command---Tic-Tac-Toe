layout = ['T','I','C','T','A','C','T','O','E']

def board_layout(layout):

    num_line = "\n""\033[37m""      1     2     3  "
    a_line = "\n\na     " + layout[0] + "  |  " + layout[1] + "  |  " + layout[2] + "  "
    ab_break = "\n    -----|-----|-----"
    b_line = "\nb     " + layout[3] + "  |  " + layout[4] + "  |  " + layout[5] + "  "
    bc_break = "\n    -----|-----|-----"
    c_line = "\nc     " + layout[6] + "  |  " + layout[7] + "  |  " + layout[8] + "  \n"

    board = num_line + a_line + ab_break + b_line + bc_break + c_line
    return print(board)


def player_1_win_check():
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if layout[win[0]] == 'X' and layout[win[1]] == 'X' and layout[win[2]] == 'X':
            layout[win[0]] = "\033[32m""X""\033[37m"
            layout[win[1]] = "\033[32m""X""\033[37m"
            layout[win[2]] = "\033[32m""X""\033[37m"
            board_layout(layout)
            print('\nPlayer 1 Wins!\n')
            return True

def player_2_win_check():
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if layout[win[0]] == 'O' and layout[win[1]] == 'O' and layout[win[2]] == 'O':
            layout[win[0]] = "\033[33m""O""\033[37m"
            layout[win[1]] = "\033[33m""O""\033[37m"
            layout[win[2]] = "\033[33m""O""\033[37m"
            board_layout(layout)
            print('\nPlayer 2 Wins!\n')
            return True

def restart():
    layout = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    board_layout(layout)
    player_1_move()

def player_1_move_played(): 
    if player_1_win_check() == True:
        ask_restart = input("Play again Y or N?")
        if ask_restart.lower() == 'Y':
            restart()
        else:
            exit
    else:
        board_layout(layout)
        player_2_move()
   
def player_2_move_played():
    if player_2_win_check() == True:
        ask_restart = input("Play again Y or N?")
        if ask_restart.lower() == 'Y':
            restart()
        else:
            exit
    else:
        board_layout(layout)
        player_1_move()

def player_1_spot_taken():
    print("\033[31m""\nSomeone has already played there!\n""\033[37m")
    player_1_move()

def player_2_spot_taken():
    print("\033[31m""\nSomeone has already played there!\n""\033[37m")
    player_2_move()

def player_1_wrong_input():
    print("\033[31m""\nThat is not a correct move!\n""\033[37m")
    player_1_move()

def player_2_wrong_input():
    print("\033[31m""\nThat is not a correct move!\n""\033[37m")
    player_2_move()

def player_1_move():
    move = input("Player 1, pick your square:")
    all_moves = [['a1', 0], ['a2', 1], ['a3', 2], ['b1', 3], ['b2', 4], ['b3', 5], ['c1', 6], ['c2', 7], ['c3', 8]]
    correct_move = False
    for moves in all_moves:
        if move.lower() == moves[0] and layout[moves[1]] == ' ':
            correct_move = True
            layout[moves[1]] = 'X'
            player_1_move_played()
        elif move.lower() == 'exit':
            correct_move = True
            exit
        elif move.lower() == moves[0] and (layout[moves[1]] == 'X' or layout[moves[1]] == 'O'):
            player_1_spot_taken()
    if correct_move == False:
        player_1_wrong_input()          
        
def player_2_move():
    move = input("Player 2, pick your square:")
    all_moves = [['a1', 0], ['a2', 1], ['a3', 2], ['b1', 3], ['b2', 4], ['b3', 5], ['c1', 6], ['c2', 7], ['c3', 8]]
    correct_move = False
    for moves in all_moves:
        if move.lower() == moves[0] and layout[moves[1]] == ' ':
            correct_move = True
            layout[moves[1]] = 'O'
            player_2_move_played()
        elif move.lower() == 'exit':
            correct_move = True
            exit
        elif move.lower() == moves[0] and (layout[moves[1]] == 'X' or layout[moves[1]] == 'O'):
            player_2_spot_taken()
    if correct_move == False:
        player_2_wrong_input()

rules = """\nPlayer 1 is X\nPlayer 2 is O\n
Each square has a letter to the left, and a number above
Enter letter first and number second to make your move
eg. a1 for the top left square, or c2 for the bottom middle square"""
start = "\nType \'Start\' to start\n"

board_layout(layout)
print(rules)
    
start_input = input(start)
if start_input.lower() == 'start':
    layout = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    board_layout(layout)
    player_1_move()

