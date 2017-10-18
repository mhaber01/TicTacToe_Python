# Sample solution for Assignment 8 - Tic Tac Toe Game


# The drawboard function is relatively straight forward. The only catch is the nested loop, and the way each row is printed in the same line.

def drawboard(board):
	for row in board:
		for col in row:
			print(col, end = " ")
		print()


# The only thing to take care of in the getcell function is checking whether r and c are outside of 0 and 2 BEFORE checking board[r][c] != '-'

def getcell(board):
	r = int(input("Enter row: "))
	c = int(input("Enter col: "))
	while (r < 0 or r > 2) or (c < 0 or c > 2) or (board[r][c] != '-'):
		r = int(input("Enter row again: "))
		c = int(input("Enter col again: "))

	return r,c


# The updateboard function really has no explanation required. symbol is the symbol to be inserted, row, and column are given... so yeah.

def updateboard(row, column, symbol, board):
	board[row][column] = symbol
	return board


# There are a ton of ways to implement checkwin. Even if you have done it by checking each possible row and column for' X' and 'O', that's fine.
# As long as you have taken care of every victory condition, you will get full credit for this.
# This is the shortest way I could come up with.
# Again, even in my way, you could change things around, as long as it logically makes sense.

def checkwin(board):

	# First we check if any row has victory condition
	# Notice the use of list.count() to simplify the condition
	for row in board:
		if row.count('X') == 3 or row.count('O') == 3:
			return True


	# We now check if any column meets the victory condition
	# Notice, the outer for loop goes through the columns (as opposed to drawboard)
	# For each column, we accumulate the contents into a string
	# Then our check condition simply becomes checking if the string is "XXX" or "OOO"
	# Also notice how we reset the test string after all the rows, before starting the next column
	columnTest = ""
	for col in range(3):
		for row in range(3):
			columnTest += board[row][col]
		if columnTest == "XXX" or columnTest == "OOO":
			return True
		columnTest = ""


	# Finally we check the diagonals.
	# Again we make 2 strings of the diagonals and check those strings to simplify our conditions.
	diagonal1 = board[0][0] + board[1][1] + board[2][2]
	diagonal2 = board[0][2] + board[1][1] + board[2][0]

	if diagonal1 == "XXX" or diagonal1 == "OOO" or diagonal2 == "XXX" or diagonal2 == "OOO":
		return True


	# If we have reached this point, none of the victory conditions were satisfied, so there is no win yet
	return False



# The function checktie, is again, not complicated
# Go through each row, and see if an empty cell ('-') exists in any row
def checktie(board):
	for row in board:
		if '-' in row:
			return False

	return True



# The startgame function is the function that runs the actual game and uses the other functions
def startgame():
	
	# Take player names as input
	p1 = input("Enter Player 1 Name: ")
	p2 = input("Enter Player 2 Name: ")
	
	# Create the empty board
	myboard = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

	# Initialize the turn variable to keep track of turn
	turn = 1

	# Start the main loop as long as there is no victory and no tie
		# Get a cell from the player
		# Call update board board based on the turn
		# Flip turn
		# Draw the board
	while (not checkwin(myboard)) and (not checktie(myboard)):

		row, col = getcell(myboard)

		if turn == 1:
			myboard = updateboard(row, col, "O", myboard)
			turn = 2
		else:
			myboard = updateboard(row, col, "X", myboard)
			turn = 1

		drawboard(myboard)


	# If we reach here, the loop has ended
	# This means either victory or tie
	# In any case, game over.
	print("Game Over")


# We must call startgame from the main program to start it off
# Notice, no printing or storing in variables
# Simple function call
startgame()










