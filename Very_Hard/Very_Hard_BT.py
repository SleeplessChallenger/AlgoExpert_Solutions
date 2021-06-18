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
