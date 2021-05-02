# 1 Boggle Board
# mine
class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = '*'
	
	def add(self, word):
		node = self.root
		for letter in word:
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = word


def boggleBoard(board, words):
    trie = Trie()
	for word in words:
		trie.add(word)
	explored = [[False for x in y] for y in board]
	result = []
	for x in range(len(board)):
		for y in range(len(board[x])):
			explore(x, y, board, result, explored, trie.root)
	return result

def explore(i, j, board, result, explored, node):
	if explored[i][j]:
		return
	letter = board[i][j]
	if letter not in node:
		return
	node = node[letter]
	explored[i][j] = True
	if '*' in node:
		if not node['*'] in result:
			result.append(node['*'])
	others = helper(i, j, board)
	for obj in others:
		explore(obj[0], obj[1], board, result, explored, node)
	explored[i][j] = False

def helper(i, j, board):
	cont = []
	if i > 0 and j > 0:
		cont.append([i - 1, j - 1])
	if i > 0 and j < len(board[0]) - 1:
		cont.append([i - 1, j + 1])
	if i < len(board) - 1 and j < len(board[0]) - 1:
		cont.append([i + 1, j + 1])
	if i < len(board) - 1 and j > 0:
		cont.append([i + 1, j - 1])
	if i > 0:
		cont.append([i - 1, j])
	if i < len(board) - 1:
		cont.append([i + 1, j])
	if j > 0:
		cont.append([i, j - 1])
	if j < len(board[0]) - 1:
		cont.append([i, j + 1])
	return cont

# not mine
class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = '*'
	
	def add(self, word):
		# in this Trie we don't create
		# substrings, but just whole words
		# will be placed separately
		node = self.root
		for letter in word:
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = word
							

def boggleBoard(board, words):
    trie = Trie()
	for word in words:
		trie.add(word)
	final = {}
	explored = [[False for x in y] for y in board]
	for idx1 in range(len(board)):
		for idx2 in range(len(board[idx1])):
			explore(idx1, idx2, board, trie.root, explored, final)
	return list(final.keys())

def explore(i, j, board, root, explored, final):
	if explored[i][j]:
		return
	letter = board[i][j]
	if letter not in root:
		return
	explored[i][j] = True
	nextNode = root[letter]
	if '*' in nextNode:
		final[nextNode['*']] = True
	neighbs = getNeigh(i, j, board)
	for token in neighbs:
		explore(token[0], token[1], board, nextNode, explored, final)
	explored[i][j] = False
	
def getNeigh(i, j, board):
	cont = []
	if i > 0 and j > 0:
		cont.append([i - 1, j - 1])
	if i > 0 and j < len(board[0]) - 1:
		cont.append([i - 1, j + 1])
	if i < len(board) - 1 and j < len(board[0]) - 1:
		cont.append([i + 1, j + 1])
	if i < len(board) - 1 and j > 0:
		cont.append([i + 1, j - 1])
	if i > 0:
		cont.append([i - 1, j])
	if i < len(board) - 1:
		cont.append([i + 1, j])
	if j > 0:
		cont.append([i, j - 1])
	if j < len(board[0]) - 1:
		cont.append([i, j + 1])
	return cont
