import random as rm

# Function to check if there are any moves left.
def isMovesLeft(board) :
	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == '_') : return True
	return False

# Function to check if any player has won the game or not.
def evaluate(b) :
	# Check for rows.
	for row in range(3) :	
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
			if (b[row][0] == player) : return 10
			elif (b[row][0] == opponent) : return -10

	# Check for columns.
	for col in range(3) :
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
			if (b[0][col] == player) : return 10
			elif (b[0][col] == opponent) : return -10

	# Check for diagonals.
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
		if (b[0][0] == player) : return 10
		elif (b[0][0] == opponent) : return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
		if (b[0][2] == player) : return 10
		elif (b[0][2] == opponent) : return -10

	return 0

# Minimax function.
def minimax(board, isMax) :
	score = evaluate(board)

	# If Maximizer has won the game return its evaluated score
	if (score == 10) : return score

	# If Minimizer has won the game return its evaluated score
	if (score == -10) : return score

	# If there are no more moves and no winner then it is a tie
	if (isMovesLeft(board) == False) : return 0

	# If this maximizer's move
	if (isMax) :	
		best = -1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
				# Check if cell is empty
				if (board[i][j]=='_') :
					# Make the move.
					board[i][j] = player
					# Call minimax recursively and choose the maximum value.
					best = max(best, minimax(board, not isMax) )
					# Undo the move
					board[i][j] = '_'
		return best

	# If this minimizer's move.
	else :
		best = 1000

		# Traverse all cells.
		for i in range(3) :		
			for j in range(3) :
				# Check if cell is empty.
				if (board[i][j] == '_') :
					# Make the move
					board[i][j] = opponent
					# Call minimax recursively and choose the minimum value.
					best = min(best, minimax(board, not isMax))
					# Undo the move.
					board[i][j] = '_'
		return best

# Function to find the best move for player.
def findBestMove(board) :
    bestVal = -1000
    bestMove = (-1, -1)

	# Traverse all cells and evaluate minimax function for all empty cells.
    for i in range(3) :	
        for j in range(3) :
			# Check if cell is empty.
            if (board[i][j] == '_') :
				# Make the move.
                board[i][j] = player
				# Find the value of current move.
                moveVal = minimax(board, False)
				# Undo the move.
                board[i][j] = '_'

				# If the value of the current move is more than the best value, then update bestVal.
                if (moveVal > bestVal) :			
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove

# Driver code
i = rm.randint(1,2) # AI chooses 'X' or 'O'

# Decide who will start the game ('X' starts the game)
if(i == 1) :
	ai = 'X'
	human = 'O'
	player = ai
	opponent = human
    
else : 
	ai = 'O'
	human = 'X'
	player = human
	opponent = ai

print("\nAI -" ,ai)
print("Human -" ,human)

board = [
	[ '_', '_', '_' ],
	[ '_', '_', '_' ],
	[ '_', '_', '_' ]
]

# Game Starts
for move in range(9) :
	print("\n---------------------------------")
	print("\nBoard is: ")
		
	for i in range(3) : print(board[i])

	print("\nThe Possible Moves are :")
	for i in range(3) :	
		for j in range(3) :
			if (board[i][j] == '_') : print("ROW:", i, " COL:", j)
	
	print("\n---------------------------------")

    # AI's Turn
	if (player == ai) :
		print("\nAI's Turn")
		bestMove = findBestMove(board)
		
		print("\nAI's Move is: ")
		print("ROW:", bestMove[0], " COL:", bestMove[1])
		board[bestMove[0]][bestMove[1]] = player

    # Human's Turn
	else :
		print("\nYour Turn")
		T = 1
		while(T > 0) :
			print("\nEnter position where you want to play: ")
			i , j = int(input("ROW: ")), int(input("COL: "))
			print("\nYour Move is: ")
			print("ROW:", i, " COL:", j)
			
			if(board[i][j] != '_') : print("\nWrong Move. Play Again!!")
			else : 
				board[i][j] = player
				break
	
	# Check if Anyone Won
	if(evaluate(board) == 10) :
		if (player == ai) : print("\nAI Won\n")
		else : print("\nYou Won\n")
		break
	
	elif(evaluate(board) == -10) : 
		if (opponent == ai) : print("\nAI Won\n")
		else : print("\nYou Won\n")
		break
	
	elif(isMovesLeft(board) == False) : 
		print("\nIt is a Tie\n")
		break

    # Decide whose turn is it now
	player, opponent = opponent, player
