# 1 Number of Binary Tree Topologies

# recursive
# see papers for detailed explanation
# of every recursive call
def numberOfBinaryTreeTopologies(n, memo={0: 1}):
    if n in memo:
		return memo[n]
	count = 0
	# if without reversed, then at first:
	# 0: leftSubtree 2: rightSubtree
	# else: 2: leftSubtree 0: rightSubtree
	for left in reversed(range(n)):
		right = n - 1 - left
		leftSubtree = numberOfBinaryTreeTopologies(left, memo)
		rightSubtree = numberOfBinaryTreeTopologies(right, memo)
		count += leftSubtree * rightSubtree
	memo[n] = count
	return count

# iterative
def numberOfBinaryTreeTopologies(n):
    cache = [1]
	for num in range(1, n + 1):
		numberOfTrees = 0
		for leftTree in range(0, num):
			leftSubtree = cache[leftTree]
			rightTree = num - 1 - leftTree
			# use `num` as we need max
			# possible amount of branches
			rightSubtree = cache[rightTree]
			numberOfTrees += leftSubtree * rightSubtree
		cache.append(numberOfTrees)
	return cache[n]

# 2 Non-Attacking Queens
# first
# number of positions where no queen can 
# attack another one in a single turn
# n: 1. number of queens 2. n*n board
def nonAttackingQueens(n):
	# idx is row and value is value
	board = [0 for _ in range(n)]
	return countPositions(board, n, 0)

def countPositions(board, n, row):
	if row == n:
		return 1
	
	count = 0
	for i in range(len(board)):
		if checkQueen(row, i, board):
			board[row] = i
			count += countPositions(board, n, row + 1)
			# !! being at first row we initially get
			# True, but if pos (0, 0) on the board
			# isn't satisfactory -> go to the next
			# iteration cycle and first Queen will be placed
			# at col 1 or any else to the right
	
	return count

def checkQueen(row, col, board):
	for i in range(row):
		# at first iteration row is 0
		# hence we return True
		prevCol = board[i]
		colCheck = prevCol != col
		diagCheck = abs(prevCol - col) != abs(row - i)
		# abs(x2 - x1) == abs(y2 - y1)
		if not colCheck or not diagCheck:
			return False
	return True

# second
# to reduce time compl. by
# making checks O(1) instead of O(n)
# we create sets: col, up diag., down diag
# BUT: when we find that it's not possible
# to put `queen` in particular position,
# we need to remove such number from set() as well

# !! (col + row) & (col - row) will help to check
# up diagonal and down diagonal respectively
def nonAttackingQueens(n):
	up = set()
	down = set()
	col = set()
	return getQueens(0, up, down, col, n)

def getQueens(row, up, down, col, n):
	if row == n:
		return 1
	
	count = 0
	for i in range(n):
		if checkPositions(i, row, up, down, col):
			fillSets(up, down, col, i, row)
			count += getQueens(row + 1, up, down, col, n)
			# after rec() fucntion terminates 
			# either due to False or other reason,
			# we need to remove data from set()
			removeSets(up, down, col, i, row)
	
	return count

def checkPositions(colIdx, row, up, down, col):
	if colIdx in col:
		return False
	if (colIdx + row) in up:
		return False
	if (row - colIdx) in down:
		return False
	
	return True

def fillSets(up, down, col, colIdx, row):
	up.add(row + colIdx)
	down.add(row - colIdx)
	col.add(colIdx)
	
def removeSets(up, down, col, colIdx, row):
	up.remove(row + colIdx)
	down.remove(row - colIdx)
	col.remove(colIdx)
