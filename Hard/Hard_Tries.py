# 1 Multi String Search
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

		
def multiStringSearch(bigString, smallStrings):
    trie = Trie()
	for word in smallStrings:
		trie.add(word)
	result = []
	for idx in range(len(bigString)):
		helper(idx, trie, bigString, result)
	return [word in result for word in smallStrings]
		
def helper(idx, trie, bigString, result):
	node = trie.root
	for idx in range(idx, len(bigString)):
		letter = bigString[idx]
		if letter not in node:
			break
		node = node[letter]
		if trie.endSymbol in node:
			result.append(node[trie.endSymbol])

			
# not mine
class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = '*'

	def insert(self, word):
		node = self.root
		for letter in word:
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = word


def multiStringSearch(bigString, smallStrings):
	trie = Trie()
	for word in smallStrings:
		trie.insert(word)
	result = {}
	for idx in range(len(bigString)):
		helper(idx, bigString, trie, result)
	return [token in result for token in smallStrings]

def helper(idx, bigString, trie, result):
	node = trie.root
	for i in range(idx, len(bigString)):
		letter = bigString[i]
		if letter not in node:
			break
		node = node[letter]
		if trie.endSymbol in node:
			result[node[trie.endSymbol]] = True
