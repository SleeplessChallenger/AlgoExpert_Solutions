# 1 Max Path Sum
def maxPathSum(tree):
	dropValue, result = helper(tree)
	return result
	
def helper(root):
    if root is None:
		return (0, float('-inf'))
	
	leftBranch, leftSum = helper(root.left)
	rightBranch, rightSum = helper(root.right)
	maxChildSumBranch = max(leftBranch, rightBranch)
	# (above) doesn't come from triangle,
	# but from a branch
	
	maxSumBranch = max(maxChildSumBranch + root.value, root.value)
	maxSumTree = max(maxSumBranch, 
					 leftBranch + rightBranch + root.value)
	currPathSum = max(leftSum, rightSum, maxSumTree)
	
	return (maxSumBranch, currPathSum)
