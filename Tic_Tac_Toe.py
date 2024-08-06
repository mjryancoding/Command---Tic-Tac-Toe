layout = ['T','I','C','T','A','C','T','O','E']

def board_layout(layout):

    num_line = "\n      1     2     3  "
    a_line = "\n\na     " + layout[0] + "  |  " + layout[1] + "  |  " + layout[2] + "  "
    ab_break = "\n    -----|-----|-----"
    b_line = "\nb     " + layout[3] + "  |  " + layout[4] + "  |  " + layout[5] + "  "
    bc_break = "\n    -----|-----|-----"
    c_line = "\nc     " + layout[6] + "  |  " + layout[7] + "  |  " + layout[8] + "  \n"

    board = num_line + a_line + ab_break + b_line + bc_break + c_line
    return print(board)

def player_1_move_played():
    board_layout(layout)
    player_2_move()

def player_2_move_played():
    board_layout(layout)
    player_1_move()

def player_1_spot_taken():
    print("Someone has already played there!")
    player_1_move()

def player_2_spot_taken():
    print("Someone has already played there!")
    player_2_move()


def player_1_move():
    move = input("Player 1, pick your square:")
    if move.lower() == 'a1' and layout[0] == ' ':
        layout[0] = 'X'
        player_1_move_played()
    elif move.lower() == 'a2' and layout[1] == ' ':
        layout[1] = 'X'
        player_1_move_played()
    elif move.lower() == 'a3' and layout[2] == ' ':
        layout[2] = 'X'
        player_1_move_played()
    elif move.lower() == 'b1' and layout[3] == ' ':
        layout[3] = 'X'
        player_1_move_played()
    elif move.lower() == 'b2' and layout[4] == ' ':
        layout[4] = 'X'
        player_1_move_played()
    elif move.lower() == 'b3' and layout[5] == ' ':
        layout[5] = 'X'
        player_1_move_played()
    elif move.lower() == 'c1' and layout[6] == ' ':
        layout[6] = 'X'
        player_1_move_played()
    elif move.lower() == 'c2' and layout[7] == ' ':
        layout[7] = 'X'
        player_1_move_played()
    elif move.lower() == 'c3' and layout[8] == ' ':
        layout[8] = 'X'
        player_1_move_played()
    elif move.lower() == 'exit':
        exit
    else:
        player_1_spot_taken()
        
def player_2_move():
    move = input("Player 2, pick your square:")
    if move.lower() == 'a1' and layout[0] == ' ':
        layout[0] = 'O'
        player_2_move_played()
    elif move.lower() == 'a2' and layout[1] == ' ':
        layout[1] = 'O'
        player_2_move_played()
    elif move.lower() == 'a3' and layout[2] == ' ':
        layout[2] = 'O'
        player_2_move_played()
    elif move.lower() == 'b1' and layout[3] == ' ':
        layout[3] = 'O'
        player_2_move_played()
    elif move.lower() == 'b2' and layout[4] == ' ':
        layout[4] = 'O'
        player_2_move_played()
    elif move.lower() == 'b3' and layout[5] == ' ':
        layout[5] = 'O'
        player_2_move_played()
    elif move.lower() == 'c1' and layout[6] == ' ':
        layout[6] = 'O'
        player_2_move_played()
    elif move.lower() == 'c2' and layout[7] == ' ':
        layout[7] = 'O'
        player_2_move_played()
    elif move.lower() == 'c3' and layout[8] == ' ':
        layout[8] = 'O'
        player_2_move_played()
    elif move.lower() == 'exit':
        exit
    else:
        player_2_spot_taken()
   


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

