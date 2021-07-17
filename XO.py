table_range = list(range(1, 10))
X_start = True
table = []
table_space = 0
def start():
    global table
    table = [" ", " ", " ",
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
    global table_space
    if X_start:
        Input = eval(input("X turn input : "))
    else:
        Input = eval(input("O turn input : "))
    if Input in table_range:
        if table[Input - 1] == " ":
            if X_start:
                table[Input - 1] = "x"
            else:
                table[Input - 1] = "o"
            table_space += 1
            X_start = not X_start
            return
        else:
            print("Can not put the mark on same tile \n")
    else:
        print("Please input number between 1 - 9 \n")
    User_input(X_start)

def Display():
    print(f" {table[0]} | {table[1]} | {table[2]}")
    print(f"-----------")
    print(f" {table[3]} | {table[4]} | {table[5]}")
    print(f"-----------")
    print(f" {table[6]} | {table[7]} | {table[8]} \n")

def check(table):
    # แนวนอน
    if table[0] == table[1] == table[2] != " ":
        return False
    if table[3] == table[4] == table[5] != " ":
        return False
    if table[6] == table[7] == table[8] != " ":
        return False
    # แนวตั้ง
    if table[0] == table[3] == table[6] != " ":
        return False
    if table[1] == table[4] == table[7] != " ":
        return False
    if table[2] == table[5] == table[8] != " ":
        return False
    # แนวทแยง
    if table[0] == table[4] == table[8] != " ":
        return False
    if table[2] == table[4] == table[6] != " ":
        return False
    if table_space == 9:
        return False
    return True
if __name__ == '__main__':
    start()
    Display()
    while check(table):
        User_input(X_start)
        X_start = not X_start
        Display()
    if table_space == 9:
        print("Draw")
    elif not X_start:
        print("Winner is x")
    else:
        print("Winner is o")
