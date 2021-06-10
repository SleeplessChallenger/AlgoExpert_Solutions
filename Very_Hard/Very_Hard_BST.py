# 1 Right Smaller Than
# two optimal solutions with T: O(n*log(n)) S: O(n)

# n - numbers smaller at insertion
# l - left subtree
# n | n l | n l | n l | n l | n l | n l
# 0 1   1 1   1 0   0 0   4 2   4 0   5 0
#  2 	 4	   3	 -1	   11 	 5     8
# `left subtree` will be added to values 
# (`.numsSmallerAtInsert`) that are 
# greater than self.value. `numbers` will
# be used eventually

# first
def rightSmallerThan(arr):
	if len(arr) == 0:
		return arr
	
	lastIdx = len(arr) - 1
	node = BST(arr[lastIdx], lastIdx, 0)
	for i in reversed(range(len(arr) - 1)):
	# `-1` as we already created one node
		node.insert(arr[i], i)
		# we'll start from root node every
		# time to calculate `smaller nodes`
		# and `left subtree`
	
	result = [0 for _ in arr]
	getResult(result, node)
	return result

def getResult(arr, root):
	if root is None:
		return
	arr[root.idx] = root.numsSmallerAtInsert
	getResult(arr, root.left)
	getResult(arr, root.right)


class BST:
	def __init__(self, value, idx, numsSmallerAtInsert, left=None, right=None):
		self.value = value
		self.idx = idx
		self.numsSmallerAtInsert = numsSmallerAtInsert
		self.left = left
		self.right = right
		self.leftSubtree = 0
	
	def insert(self, value, idx, smaller=0):
		if self.value > value:
			self.leftSubtree += 1
			if self.left is None:
				self.left = BST(value, idx, smaller)
			else:
				self.left.insert(value, idx, smaller)
		else:
			smaller += self.leftSubtree
			if value > self.value:
				smaller += 1
			if self.right is None:
				self.right = BST(value, idx, smaller)
			else:
				self.right.insert(value, idx, smaller)

# second
def rightSmallerThan(arr):
    if len(arr) == 0:
		return arr
	
	result = arr[:]
	lastIdx = len(arr) - 1
	node = BST(arr[lastIdx])
	result[lastIdx] = 0
	for i in reversed(range(len(arr) - 1)):
		node.insert(arr[i], i, result)
	
	return result


class BST:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.leftSubtree = 0
		self.left = left
		self.right = right
	
	def insert(self, value, idx, res, smaller=0):
		if self.value > value:
			self.leftSubtree += 1
			if self.left is None:
				self.left = BST(value)
				res[idx] = smaller
			else:
				self.left.insert(value, idx, res, smaller)
		else:
			smaller += self.leftSubtree
			if value > self.value:
				smaller += 1
			if self.right is None:
				self.right = BST(value)
				res[idx] = smaller
			else:
				self.right.insert(value, idx, res, smaller)

# brute-force. T: O(n^2) S: O(n)
def rightSmallerThan(arr):
	new = [0 for _ in arr]
    for up in range(len(arr)):
		curr = arr[up]
		for down in range(up + 1, len(arr)):
			compare = arr[down]
			if curr > compare:
				new[up] += 1
	
	return new
