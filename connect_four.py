def main():
    #this is ugly as hell, good lord
    #don't do this, initialize it with a nested for loop
    board = [["~" for number in range(1,8)],["~" for number in range(1,8)],["~" for number in range(1,8)]
    ,["~" for number in range(1,8)],["~" for number in range(1,8)],["~" for number in range(1,8)]]
   
    winner = 0
    game_start = True

    while 1:
        for i in range(1,3):
            if game_start:
                printBoard(board)
                game_start = False
            _drop(board, i)
            printBoard(board)
            winner = check_win(board)
            game_start = reset_game(winner,board,game_start)
   
def printBoard(_board):

    labels = [str(i) for i in range(1,8)]

    print("\n")
    print(labels)

    for i in range(0,6):
        print(_board[i])

def _drop(_board, player):

    while 1:

        flag = True

        try:

            while flag:
                row = ord(input("Player " + str(player) + " Pick a row to drop[1-7]: ")) #using ord over int so try except catches letters
                
                if row >= 49: #prevents negative indexs
                    row -= 49
                
            

            
                    for i in range(1,6):
                            
                        if _board[i][row] == "X" or _board[i][row] == "O":
                            if not _board[i-1][row] == "X" and not _board[i-1][row] == "O":
                                if player == 1:
                                    _board[i-1][row] = "X"
                                    flag = False
                                    break
                                else:
                                    _board[i-1][row] = "O"
                                    flag = False
                                    break
                            else:
                                print("\nSpot taken, pick another. \n")
                                break
                        if i == 5:
                            if player == 1:
                                _board[i][row] = "X"
                                flag = False
                                break
                            else:
                                _board[i][row] = "O"
                                flag = False
                                break
        except:
            print("Invalid input.")
        if not flag:
            break

def check_win(_board):
    p1win = 0
    p2win = 0

    if "~" not in _board[0]: #if first element is full of X and O then all subsequent elements are also full
        return 3
        


    for i in range(0,7):
        p1win = 0
        p2win = 0
        for j in range(0,6):
            if _board[j][i] == "X":
                p1win += 1
            else:
                p1win = 0
            if _board[j][i] == "O":
                p2win += 1
            else:
                p2win = 0

            if p1win == 4:
                return 1
            if p2win == 4:
                return 2


    for i in range(0,6):
        p1win = 0
        p2win = 0
        for j in range(0,7):
            if _board[i][j] == "X":
                p1win += 1
            else:
                p1win = 0
            if _board[i][j] == "O":
                p2win += 1
            else:
                p2win = 0

            if p1win == 4:
                return 1
            if p2win == 4:
                return 2

    if test_diagonal_r(_board) == 1 or test_diagonal_r(_board) == 2:
        return test_diagonal_r(_board)

    if test_diagonal_l(_board) == 1 or test_diagonal_l(_board) == 2:
        return test_diagonal_l(_board)

def test_diagonal_r(_board):
    count = 4
    change = True
    x = 2 #coordinate names are backwards
    y = 0
    y_count = 0
    p1win = 0
    p2win = 0
    temp_x = x
    temp_y = y

    while count > 3:
        
            
        p1win = 0
        p2win = 0
        
        while temp_x < x+count:
            if _board[temp_x][temp_y] == "X":
                p1win += 1
            else:
                p1win = 0
            if _board[temp_x][temp_y] == "O":
                p2win += 1
            else:
                p2win = 0

            if p1win == 4:
                return 1
            if p2win == 4:
                return 2

            temp_x += 1
            temp_y += 1

        if x > 0:
            x -= 1
            
        if y_count > 1:
            y += 1
        else:
            y_count += 1

        if change:
            count += 1
            if count == 7:
                count -=1
                change = False
        else:
            count -= 1
        temp_x = x
        temp_y = y
    return 0

def test_diagonal_l(_board):
    count = 4
    change = True
    x = 3 #coordinate names are backwards
    y = 0
    y_count = 0
    p1win = 0
    p2win = 0
    temp_x = x
    temp_y = y

    while count > 3:
        
            
        p1win = 0
        p2win = 0
        
        while temp_x > x-count:
            if _board[temp_x][temp_y] == "X":
                p1win += 1
            else:
                p1win = 0
            if _board[temp_x][temp_y] == "O":
                p2win += 1
            else:
                p2win = 0

            if p1win == 4:
                return 1
            if p2win == 4:
                return 2

            temp_x -= 1
            temp_y += 1

        if x < 5:
            x += 1
            
        if y_count > 1:
            y += 1
        else:
            y_count += 1

        if change:
            count += 1
            if count == 7:
                count -=1
                change = False
        else:
            count -= 1
        temp_x = x
        temp_y = y
    return 0

def reset_game(win, _board, start):

    replay = "y"

    if win == 1 or win == 2 or win == 3:

        if win == 3:
            replay = input("Draw! Play again?(y/n): ")
        else:
            replay = input("Player " + str(win) + " wins! Play again?(y/n): ")
        for i in range(0,6):
            for j in range(0,7):
                _board[i][j] = "~"
        
        if not (replay == "Y" or replay == "y"):
            exit(1)
        return True
    else:
        return False

main()

    