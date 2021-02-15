# 1 Branch sums
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# a
def branchSums(root):
	# we don't use return in helper 
	# as we store in variable
	arr = []
	def helper(root, temp):
		temp += root.value
		if root.left:
			helper(root.left, temp)
		if root.right:
			helper(root.right, temp)
		if root.left is None and root.right is None:
			arr.append(temp)
	helper(root, 0)
	return arr

# b
def branchSums(root):
	result = []
	def traverse(root, temp):
		newTemp = temp + root.value
		if root.left:
			traverse(root.left, newTemp)
		if root.right:
			traverse(root.right, newTemp)
		if root.left is None and root.right is None:
			result.append(newTemp)
	traverse(root, 0)
	return result

# 2 Node depths
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root, depth=0):
	if root is None:
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
