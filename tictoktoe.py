board=["A0","A1","A2",

       "B3","B4","B5",

       "C6","C7","C8"]
current_player="X"
winner=None
game_is_going=True
print("the game is start")

def display_board():
    print(board[0] +" "+ "|" +" "+ board[1] +" "+ "|" +" "+ board[2])
    print("-------------")
    print(board[3] +" "+ "|" +" "+ board[4] +" "+ "|" +" "+ board[5])
    print("-------------")
    print(board[6] +" "+ "|" +" "+ board[7] +" "+ "|" +" "+ board[8])
    print("\n")
    print("***************************************")

def handle_turn():
    position=int(input("enter the position from 0 to 8:",))
    print("***************************************\n")
    board[position]=current_player
    display_board()

def play_game():
    display_board()
    global position

    while game_is_going:
        handle_turn()

        flip_player()

        check_if_winner()

    if winner=="X" or winner=="O":
        print("winner is",winner)



def check_if_winner():
    global winner
    row_winner=check_row()
    col_winner=check_col()
    dia_winner=check_dia()
    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    elif dia_winner:
        winner=dia_winner



def check_row():
    global game_is_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game_is_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_col():
    global game_is_going
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'
    if col_1 or col_2 or col_3:
        game_is_going=False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]


def check_dia():
    global game_is_going
    dia_1 = board[0] == board[4] == board[8] != '-'
    dia_2 = board[2] == board[4] == board[6] != '-'
    if dia_1 or dia_2:
        game_is_going=False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
play_game()





