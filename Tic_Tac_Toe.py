
def board_layout(a1,a2,a3,b1,b2,b3,c1,c2,c3):

    num_line = "\n      1     2     3  "
    a_line = "\n\na     " + a1 + "  |  " + a2 + "  |  " + a3 + "  "
    ab_break = "\n    -----|-----|-----"
    b_line = "\nb     " + b1 + "  |  " + b2 + "  |  " + b3 + "  "
    bc_break = "\n    -----|-----|-----"
    c_line = "\nc     " + c1 + "  |  " + c2 + "  |  " + c3 + "  \n"

    board = num_line + a_line + ab_break + b_line + bc_break + c_line
    return board

rules = """\nPlayer 1 is X\nPlayer 2 is O\n
Each square has a letter to the left, and a number above
Enter letter first and number second to make your move
eg. a1 for the top left square, or c2 for the bottom middle square"""
start = "\nType \'Start\' to start\n"

print(board_layout('T','I','C','T','A','C','T','O','E'))
print(rules)

    
start_input = input(start)

player_1_move = ""
player_2_move = ""

if start_input.lower() == 'start':
    print(board_layout(' ',' ',' ',' ',' ',' ',' ',' ',' '))
    player_1_move = input("Player 1, pick your square:")
