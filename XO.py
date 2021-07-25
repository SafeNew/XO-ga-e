board_range = list(range(1, 10))    # [1,2,3,4,5,6,7,8,9]
X_start = True
board = []
board_space = 0
def setup():
    global board
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " ", ]
    print("Please Input number between 1 - 9 \n")
    print(f" {1} | {2} | {3}")
    print(f"-----------")
    print(f" {4} | {5} | {6}")
    print(f"-----------")
    print(f" {7} | {8} | {9} \n")
    print("-- game start -- \n")

def User_input(X_start):
    global board_space
    if board_space == 9:
        return
    try:
        if X_start:
            Input = int(input("X turn input : "))
        else:
            Input = int(input("O turn input : "))
    except:
        Input = 0
    if Input in board_range:
        if board[Input - 1] == " ":
            if X_start:
                board[Input - 1] = "x"
            else:
                board[Input - 1] = "o"
            board_space += 1
            return
        else:
            print("Can not put the mark on same tile \n")
    else:
        print("Please input number between 1 - 9 \n")
    User_input(X_start)

def Display():
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f"-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f"-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_wining(board):
    # แนวนอน
    if board[0] == board[1] == board[2] != " ":
        return False, False
    elif board[3] == board[4] == board[5] != " ":
        return False, False
    elif board[6] == board[7] == board[8] != " ":
        return False, False
    # แนวตั้ง
    elif board[0] == board[3] == board[6] != " ":
        return False, False
    elif board[1] == board[4] == board[7] != " ":
        return False, False
    elif board[2] == board[5] == board[8] != " ":
        return False, False
    # แนวทแยง
    elif board[0] == board[4] == board[8] != " ":
        return False, False
    elif board[2] == board[4] == board[6] != " ":
        return False, False
    if board_space >= 9:
        return False, True
    return True, False
if __name__ == '__main__':
    setup()
    Display()
    while check_wining(board)[0]:
        User_input(X_start)
        X_start = not X_start
        Display()
    if check_wining(board)[1]:
        print("Draw")
    elif not X_start:
        print("Winner is x")
    else:
        print("Winner is o")
