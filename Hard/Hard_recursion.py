# 1 Lowest Common Manager
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

class Help:
	def __init__(self, manager, num):
		self.manager = manager
		self.num = num


def getLowestCommonManager(topManager, reportOne, reportTwo):
	return helper(topManager, reportOne, reportTwo).manager

def helper(top, nodeOne, nodeTwo):
	idx = 0
	for branch in top.directReports:
		result = helper(branch, nodeOne, nodeTwo)
		if result.manager:
			return result
		if result.num > 0:
			idx += result.num

	if top == nodeOne or top == nodeTwo:
		idx += 1
	boss = top if idx == 2 else None

	return Help(boss, idx)

# 2 Interweaving Strings
# T: O(2^(n + m)) S: O(n + m)
def interweavingStrings(one, two, three):
	if len(one) + len(two) != len(three):
		return False
	
	return helper(0, 0, 0, one, two, three)

def helper(i, j, k, one, two, three):
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		if helper(i + 1, j, k + 1, one, two, three):
		# `if` for the case when response is False
		# hence we switch to the next `if`
			return True
	if j < len(two) and two[j] == three[k]:
		return helper(i, j + 1, k + 1, one, two, three)
		# here `if` is useless as we simply sift down
		# to False if a) conditions above aren't met
		# b) we came back from all recursive calls
	return False

# T: O(nm) S: O(nm)
def interweavingStrings(one, two, three):
	if len(one) + len(two) != len(three):
		return False
	
	memo = [[None for x in range(len(two) + 1)]
		   	for y in range(len(one) + 1)]
	# `+1` is because there can be cases
	# when one of the indicies > len() of str
	return helper(0, 0, 0, one, two, three, memo)

def helper(i, j, k, one, two, three, memo):
	if memo[i][j] is not None:
		return memo[i][j]
	
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		memo[i][j] = helper(i + 1, j, k + 1, one, two, three, memo)
		if memo[i][j]:
		# `if` for the case when response is False
		# hence we switch to the next `if`
			return True
	if j < len(two) and two[j] == three[k]:
		memo[i][j] = helper(i, j + 1, k + 1, one, two, three, memo)
		return memo[i][j]
		# here `if` is useless as we simply sift down
		# to False if a) conditions above aren't met
		# b) we came back from all recursive calls
	memo[i][j] = False
	return False

# 3 Solve Sudoku
def solveSudoku(board):
	solvePart(0, 0, board)
	return board

def solvePart(row, col, board):
	if col == len(board[row]):
		col = 0
		row += 1
		if row == len(board):
			return True

	if board[row][col] == 0:
		return tryAtIndex(row, col, board)

	return solvePart(row, col + 1, board)

def tryAtIndex(row, col, board):
	for i in range(1, 10):
		if isValid(i, row, col, board):
			board[row][col] = i
			if solvePart(row, col + 1, board):
				return True

	board[row][col] = 0
	return False

def isValid(i, row, col, board):
	rowValid = i not in board[row]
	colValid = i not in map(lambda x: x[col], board)

	if not rowValid or not colValid:
		return False

	# 1 // 3 -> 0
	# 5 // 3 -> 1
	# 7 // 3 -> 2
	rowGrid = row // 3
	colGrid = col // 3

	for r in range(3):
		for c in range(3):
			rowCheck = rowGrid * 3 + r
			colCheck = colGrid * 3 + c
			existValue = board[rowCheck][colCheck]
			
			if i == existValue:
				return False
	return True

# 4 Generate Div Tags
def generateDivTags(numberOfTags):
	op = numberOfTags
	cl = numberOfTags
	result = []
	helper(op, cl, result, "")
	return result

def helper(op, cl, result, string):
	if op > 0:
		helper(op - 1, cl, result, string + '<div>')
	if op < cl:
		helper(op, cl - 1, result, string + '</div>')

	if cl == 0:
		result.append(string)
