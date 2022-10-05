#move the knight to the chess board such that it cover every squre (cell) of the chess board.

# we will go with the move with the lowest no. of possiblity to move.

#creating a chess baord
chess_board = [[1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]


def printBoard():
    for i in range(8):
        for j in range(8):
            print(chess_board[i][j], end=" ")
        print("\n")




def get_possibilities(x, y):
    #possibilities where knight can move
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1) #posiblity of moving around horizontal
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2) #possbility of moving around vertical
    possibilities = []
    for i in range(8):
        #checking if the cell we are moving to, is part of board.
        if x+pos_x[i] >= 0 and x+pos_x[i] <= 7 and y+pos_y[i] >= 0 and y+pos_y[i] <= 7 and chess_board[x+pos_x[i]][y+pos_y[i]] == 0:
            possibilities.append([x+pos_x[i], y+pos_y[i]])

    return possibilities

#below function is helping us to find out which function has minimum
def solve():
    counter = 2
    x = 0
    y = 0
    for i in range(63):
        pos = get_possibilities(x, y)
        minimum = pos[0]
        for p in pos:
            #finding the new minimum
            if len(get_possibilities(p[0], p[1])) <= len(get_possibilities(minimum[0], minimum[1])):
                minimum = p
        #current position of knight
        x = minimum[0]
        y = minimum[1]
        chess_board[x][y] = counter
        counter += 1

solve()    
printBoard()