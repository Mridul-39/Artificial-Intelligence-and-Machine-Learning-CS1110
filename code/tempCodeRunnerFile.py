# rules
#1. every row should have one queen
#2. every column should have one queen
#3. none of them should attack each other.

# keping track of column 
# positive diagonal = row + column
# negative diagonal = row - column

# taking value of variabe n form the user
n = int(input("Please enter value of n: "))
# creating a  list 'board' which represent n*n chess board.
board= []

# This funtion use to define the board on which we are going to work on.
# we are creating n lists  having n elements in them and each element is going to assign to 0 and queen  will be assigned 1.
def getBoard():
    for i in range(n):
        nthList =[]
        for j in range(n):
        # adding  n no. of 0 to the nthList
            nthList.append(0)
        # adding list to the board
        board.append(nthList) 


# To print the board
def printBoard():
    for i in range (n):
        for j in range (n):
            print(board[i][j], end ='')
        print(" ")

def isSafe(row, col):
    for i in range(n):
        if board[row][i] == 1:
            return False
    for j in range(n):
        if board[col][i] == 1:
            return False


    i = row-1
    j = col-1
    while(i>=0 and j>=0):
            if board[i][j] == 1:
                return False
            i = i-1
            j = j-1

    i = row-1
    j = col+1
    while(i>=0 and j<n):
            if board[i][j] == 1:
                return False
            i = i-1
            j = j+1

    i = row+1
    j = col-1
    while(i<n and j>=0):
            if board[i][j] == 1:
                return False
            i = i+1
            j = j-1

    i = row+1
    j = col+1
    while(i<n and j<n):
            if board[i][j] == 1:
                return False
            i = i+1
            j = j+1
    return True

def Put(n, count):
    if count == n:
        return True
    for i in range(n):
        for j in range(n):
            if isSafe(i, j):
                board[i][j] = 1
                count = count+1
                if Put(n, count) == True:
                    return True
                board[i][j] = 0
                count = count-1
    return False

getBoard()
Put(n, 0)
printBoard()

