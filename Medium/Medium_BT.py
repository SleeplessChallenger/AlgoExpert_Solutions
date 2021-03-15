# 1 Invert Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# recursive
def invertBinaryTree(tree):
	if tree is None:
		return
	tree.left, tree.right = tree.right, tree.left
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

# iterative
def invertBinaryTree(tree):
	queue = [tree]
	while len(queue) != 0:
		node = queue.pop(0)
		if node is None:
			continue
		node.left, node.right = node.right, node.left
		queue += [node.left, node.right]

# 2 Height Balanced Binary Tree
# a
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def heightBalancedBinaryTree(root):
	def dfs(node):
		if node is None:
			return 0
		return  1 + max(dfs(node.left), dfs(node.right))

	if root is None:
		return True

	return abs(dfs(node.left) - dfs(node.right)) <= 1 and \
		   heightBalancedBinaryTree(root.left) and \
		   heightBalancedBinaryTree(root.right)

# b
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
	def __init__(self, balanced, height):
		self.balanced = balanced
		self.height = height


def heightBalancedBinaryTree(tree):
	temp = dfs(tree)
	return tree.balanced

def dfs(node):
	if node is None:
		return TreeInfo(True, -1)

	left = dfs(node.left)
	right = dfs(node.right)

	balance = left.balanced and \
			  right.balanced and \
			  abs(left.height - right.height) \
			  <= 1
	height = 1 + max(left.height, right.height)

	return TreeInfo(balance, height)

# 3 Find successor
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# Space O(n)
def findSuccessor(tree, node):
	arr = []
	def dfs(tree, arr):
		if tree.left:
			dfs(tree.left, arr)
		arr.append(tree)
		if tree.right:
			dfs(tree.right, arr)
	dfs(tree, arr)

	for x in range(len(arr)):
		if x == len(arr) - 1:
			return None
		if arr[x] == node:
			return arr[x + 1]

# Space O(1)
def findSuccessor(tree, node):
	if node.right:
		return func1(node.right)
	return func2(node)

def func1(temp):
	while temp.left:
		temp = temp.left
	return temp

def func2(temp):
	while temp.parent and temp.parent.right == temp:
		temp = temp.parent
	return temp.parent

# 4 Binary Tree Diameter
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Help:
	def __init__(self, height, diameter):
		self.height = height
		self.diameter = diameter

# mine
def binaryTreeDiameter(tree):
	def dfs(node):
		if node is None:
			return Help(0,0)

		l = dfs(node.left)
		r = dfs(node.right)

		longest = l.height + r.height
		curr_diameter = max(l.diameter, r.diameter)

		diameter = max(longest, curr_diameter)
		height = max(l.height, r.height) + 1

		return Help(height, diameter)

	return dfs(tree).diameter

# not mine
def binaryTreeDiameter(tree):
	return dfs(tree).diameter

def dfs(node):
	if node is None:
		return Help(0, 0)
	
	l = dfs(node.left)
	r = dfs(node.right)
	# after leaves
	longest = l.height + r.height 
	# (above) through the root
	curr_diameter = max(l.diameter, r.diameter)
	# (above) maximum diameter from one of the subtree
	diameter = max(longest, curr_diameter)
	# (above) new max diameter
	height = max(l.height, r.height) + 1
	
	return Help(height, diameter)
