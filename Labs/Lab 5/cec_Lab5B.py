import copy
def initialize_board(num_rows,num_cols): #takes the numrows and numcolumns from user input and set each spot on the list to a "-"
    columnlist=[] #initializes the list for the column length of the board
    boardlist=[] #initializes the list for the entire board
    for i in range (1,num_cols+1): #loops the amount of columns and adds a blank spot "-" to the board
        columnlist.append("-")
    for n in range (1,num_rows+1): #loops through the amount of rows and adds a nested column list to a new list called "boardlist"
        boardlist.append(copy.deepcopy(columnlist)) #appends a deep copy of the columnlist to the boardlist, giving it its own variable sets each time
    return boardlist

def print_board(board): #takes in the 2D character list of the board and prints it
    index=0
    while index!=len(board): #as long as the "index" variable does not equal the actual length of the board, the nested for loop will keep executing
        for i in board[index]: #loops through the current iteration of the slice in the nested lists, printing out each item
            print(i," ",end="")
        index += 1 #"index" variable increases by as long as it does not equal the actual length of the board, allowing more columns to be printed.
        print()

def insert_chip(board,col,chip_type): #places either player 1 or 2 token in the board list based on column position and whether or not it's filled. loops until an open spot is available
    slice=0
    while True:
        if board[slice][col]=="-": #if current iteration of the slice has a blank spot in the column, replace "-" with the chip type.
            board[slice][col]=chip_type
            break
        slice+=1
    return board

def check_if_winner(board,col,row,chip_type):
    columnlist=[] #column list is initialized, adding all items in the previously selected column to a list
    slice=0 #slice variable is initialized. allows an easy way to go through each slice in a loop
    connectfour=0

    for i in board: #check for vertical win
        columnlist.append(board[slice][col]) #appends each item in a specific column to a list based on the amount of slices in the main board list
        slice+=1 #goes through each slice in each iteration of the loop

    if columnlist.count(chip_type)>=4: #if there are at least four of the same chip type in the column list, check to see whether or not they're next to each other
        for i in columnlist:
            if i==chip_type: #if chips are next to each other, connectfour should add up to 4 eventually
                connectfour+=1
                if connectfour == 4: #if connectfour reaches 4, return true
                    return True
            else: #if chips aren't next to each other, connectfour will never add up to four and keep being reset to 0.
                connectfour=0

    connectfour=0 #connectfour and slice variables are reset just incase the vertical win test was executed
    slice=0
    for i in board: #check for horizontal win
        row=[] #row list is reset on each new iteration of the for loop
        for n in board[slice]:
            row.append(n) #appends all items in a slice of the board list to the row list
            if row.count(chip_type) >= 4:  # if there are at least four of the same chip type in the row list, check to see whether or not they're next to each other
                for i in row:
                    if i == chip_type:  # if chips are next to each other, connectfour should add up to 4 eventually
                        connectfour += 1
                        if connectfour == 4:  # if connectfour reaches 4, return true
                            return True
                    else:  # if chips aren't next to each other, connectfour will never add up to four and keep being reset to 0.
                        connectfour = 0
        slice += 1
    return False #if none of the other conditions are met, return false by default.

def check_if_draw(board): #checks whether or not there is a draw
    fullslice = 0
    slice = 0
    for i in board:
        if board[slice].count("-") == 0:  # goes through each slice and checks the amount of blank spots.
            fullslice += 1  # if there are no blank spots, the total amount of full slices increases by 1
            slice += 1
        if fullslice == len(board):  # if the amount of full slices equals the length of the board list itself, it's a draw.
            return True


def main():
    numrows = int(input("What would you like the height of the board to be? ")) #takes user input for desired number of rows
    numcolumns = int(input("What would you like the length of the board to be? ")) #takes user input for desired number of columns
    boardlist= initialize_board(numrows, numcolumns)  # initializes the board's list based on what's input
    print_board(boardlist)  # prints the board based on the board list
    print("\nPlayer 1: x\nPlayer 2: o")

    while True: #initial loop that keeps switching between players 1 and 2 until there's a winner
        column=int(input("\nPlayer 1: Which column would you like to choose? ")) #player 1 input
        boardlist.reverse() #reverses the list and places it into the insert_chip function, allowing chips to be added from bottom up
        boardlist=insert_chip(boardlist,column,"x")
        boardlist.reverse() #re-reverses the list so it can be printed correctly
        print_board(boardlist)
        if check_if_winner(boardlist, column, [], "x") == True: #if player 1 wins, stop the loop
            print("\nPlayer 1 won the game!")
            break
        if check_if_draw(boardlist)==True: #if a draw is determined, stop the loop
            print("\nDraw. Nobody wins.")
            break

        column = int(input("\nPlayer 2: Which column would you like to choose? ")) #player 2 input
        boardlist.reverse()  # reverses the list and places it into the insert_chip function, allowing chips to be added from bottom up
        boardlist = insert_chip(boardlist, column, "o")
        boardlist.reverse()  # re-reverses the list so it can be printed correctly
        print_board(boardlist)
        if check_if_winner(boardlist,column,[],"o") == True: #if player 2 wins, stop the loop
            print("\nPlayer 2 won the game!")
            break
        if check_if_draw(boardlist)==True:
            print("\nDraw. Nobody wins.")
            break


#checking to make sure the program is the main one when ran
if __name__=="__main__":
    main()