# 1 Iterative In-Order Traversal
def iterativeInOrderTraversal(tree, callback):
    curr = tree
	prev = None
	while curr:
		if prev is None or prev == curr.parent:
			if curr.left:
				nextNode = curr.left
			else:
				callback(curr)
				nextNode = curr.right if curr.right is not None\
									  else curr.parent
		elif curr.left == prev:
			callback(curr)
			nextNode = curr.right if curr.right is not None\
								  else curr.parent
		# Ex: when curr at `4` and prev at `9`
		# elif prev == curr.right:
		else:
			nextNode = curr.parent
		prev = curr
		curr = nextNode

# 2 Flatten Binary Tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# T: O(n) S: O(n)
def flattenBinaryTree(root):
	arr = []
    def dfs(root, arr):
		if root.left:
			dfs(root.left, arr)
		arr.append(root)
		if root.right:
			dfs(root.right, arr)
	dfs(root, arr)
	for x in range(1, len(arr)):
		prevNode = arr[x - 1]
		currNode = arr[x]
		prevNode.right = currNode
		currNode.left = prevNode
	return arr[0]

# T: O(n) S: O(d)
def flattenBinaryTree(root):
	newRoot, _ = flattenTree(root)
	return newRoot

def flattenTree(root):
	if root.left is None:
		leftmostNode = root
	else:
		leftSubTreeLeftmost, leftSubTreeRightMost = flattenTree(root.left)
		createConnection(leftSubTreeRightMost, root)
		leftmostNode = leftSubTreeLeftmost
	
	if root.right is None:
		rightmostNode = root
	else:
		rightSubTreeLeftmost, rightSubTreeRightMost = flattenTree(root.right)
		createConnection(root, rightSubTreeLeftmost)
		rightmostNode = rightSubTreeRightMost
	
	return (leftmostNode, rightmostNode)	
	
def createConnection(left, right):
	left.right = right
	right.left = left

# 3 Right Sibling Tree
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    traverse(root, None, None)
	return root

def traverse(node, p, leftTrue):
	if node is None:
		return
	left, right = node.left, node.right
	traverse(left, node, True)
	
	if p is None:
		# to deal when we're at root
		node.right = None
	elif leftTrue:
		# as we call `traverse()` on the left
		# subtree first, then we won't overwrite
		# `.right` pointer and it'll still point
		# at `.right` INITIAL value
		node.right = p.right
	else:
		if p.right is None:
			# Ex: when we're at `9`,
			# parent is `4`. Let's suppose
			# it doesn't have `5` as `.right`
			# hence calling `parent.right.left`
			# will give error. Use this condition
			# to bypass it.  
			# Viable example: `3` has `1` as parent,
			# `7` has `3` as parent. None of those parents
			# have `.right.left` + before we reach `7`, `3`
			# will be as right node as well. `1` initially being
			# `node` will have `.right` = None, hence `3` will also
			# have `.right` = None. Hence `7` will resemble
			node.right = None
		else:
	        node.right = p.right.left
		
	traverse(right, node, False)

# 4 All Kinds of Node Depths
# mine
# T: O(n*log(n)) S: O(n)
def allKindsOfNodeDepths(root):
	arr = []
	def dfs(node, arr):
		arr.append(nodeDepth(node))
		if node.left:
			dfs(node.left, arr)
		if node.right:
			dfs(node.right, arr)
	dfs(root, arr)
	return sum(arr)

def nodeDepth(node, depth=0):
	if node is None:
		return 0
	return depth + nodeDepth(node.left, depth+1) + \
			nodeDepth(node.right, depth+1)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 2  solutions which are not mine, but same complexity
# 2-1
def allKindsOfNodeDepths(root):
	count = 0
	stack = [root]
	while len(stack) != 0:
		node = stack.pop()
		if node is None:
			continue
		count += nodeDepth(node)
		stack.append(node.left)
		stack.append(node.right)

# 2-2
def allKindsOfNodeDepths(root):
	if root is None:
		return 0
	return allKindsOfNodeDepths(root.left) +\
		   allKindsOfNodeDepths(root.right) +\
		   nodeDepth(root)

# T: O(n) S: O(n)
def allKindsOfNodeDepths(root):
    ht = {}
	countNodes(root, ht)
	htD = {}
	countDepths(root, ht, htD)
	return getResult(htD, root)

def getResult(ht, node):
	if node is None:
		return 0
	return getResult(ht, node.left) +\
		   getResult(ht,  node.right) +\
		   ht[node]
	
def countNodes(node, ht):
	# build every node `count` starting
	# from bottom (we go till bottom and
	# then start from there). Also, before
	# looking for `.left`. or. `.right` we need
	# to place `1` as current node is 1 count.
	ht[node] = 1
	if node.left:
		countNodes(node.left, ht)
		ht[node] += ht[node.left]
	if node.right:
		countNodes(node.right, ht)
		ht[node] += ht[node.right]

def countDepths(root, ht, htD):
	# from `2` as root: 2 + 2 + 1 + 1 + 0
	# from `1` as root: 3 + 3 + 2 + 2 + 1
	# or we can use `2 + 2 + 1 + 1 + 0` but instead
	# of 0 add number of nodes in the subtree.
	htD[root] = 0
	if root.left:
		countDepths(root.left, ht, htD)
		htD[root] += ht[root.left] + htD[root.left]
	if root.right:
		countDepths(root.right, ht, htD)
		htD[root] += ht[root.right] + htD[root.right]

# 5 Compare Leaf Traversal

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# T: O(n + m) S: O(n + m)
def compareLeafTraversal(tree1, tree2):
    treeOneLeaves = dfs(tree1, [])
	treeTwoLeaves = dfs(tree2, [])

	if len(treeOneLeaves) != len(treeTwoLeaves):
		return False
	
	return all(map(lambda x, y: x == y, treeOneLeaves, treeTwoLeaves)) 
	
def dfs(tree, arr):
	if tree.left:
		dfs(tree.left, arr)
	if tree.right:
		dfs(tree.right, arr)
	
	if not tree.left and not tree.right:
		arr.append(tree.value)
	
	return arr

# T: O(n + m) S: O(h1 + h2)
def compareLeafTraversal(tree1, tree2):
    stack1 = [tree1]
	stack2 = [tree2]
	
	while len(stack1) != 0 and len(stack2) != 0:
		currLeave1 = getLeave(stack1)
		currLeave2 = getLeave(stack2)
		
		if currLeave1.value != currLeave2.value:
			return False
		
	return len(stack1) == 0 and len(stack2) == 0
	
def getLeave(stack):
	node = stack.pop()
	
	while not isLeaf(node):
		# right first because 
		# we want .left to be
		# popped at first
		if node.right:
			stack.append(node.right)
			
		if node.left:
			stack.append(node.left)

		node = stack.pop()
		
	return node
	
def isLeaf(node):
	# if at least one is not None -> False
	# hence it's not a leaf and we'll
	# continue our loop in `getLeave`
	return node.right is None and node.left is None
