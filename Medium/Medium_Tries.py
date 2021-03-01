# 1 Suffix Trie Construction
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

# mine
	def populateSuffixTrieFrom(self, string):
		for x in range(len(string)):
			node = self.root
			for y in range(x, len(string)):
				if string[y] not in node:
					node[string[y]] = {}
				node = node[string[y]]
			node[self.endSymbol] = True

	def contains(self, string):
		node = self.root
		for x in rane(string):
			if string[x] not in node:
				return False
			node = node[x]
		return self.endSymbol in node

# not mine
	def populateSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insert(i, string)

	def insert(self, i, string):
		node = self.root
		for y in range(i, len(string)):
			letter = string[y]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = True

	def contains(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return self.endSymbol in node
