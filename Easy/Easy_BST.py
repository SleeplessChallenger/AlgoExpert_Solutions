# 1 Find closest value in BST
# iterative
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosest(tree, target):
	temp = float('inf')
	while tree:
		if abs(tree.value - target) < abs(target - temp):
			temp = tree.value
		if tree.value < target:
			tree = tree.right
		elif tree.value > target:
			tree = tree.left
		else:
			break
	return temp

# recursive
def findClosest(tree, target):
	def helper(tree, target, min_):
		if tree is None:
			return min_
		if abs(tree.value - target) < abs(target - min_):
			min_ = tree.value
		if target < tree.value:
			return helper(tree.left, target, min_)
		elif target > tree.value:
			return helper(tree.right, target, min_)
		else:
			return min_
	x = helper(tree, target, tree.value)
	return x
