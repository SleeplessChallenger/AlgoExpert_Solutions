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

# 2 Find Nodes Distance K
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
	

def findNodesDistanceK(root, target, k):
	parents = {}
	createParents(root, parents)
	node = getNode(parents, root, target)
	return bfs(node, parents, k)

def bfs(node, parents, k):
	queue = [[node, 0]]
	explored = {}
	explored[node] = True
	while len(queue) != 0:
		curr, dist = queue.pop(0)
		
		if dist == k:
			result = [node[0].value for node in queue]
			# as we popped the one node above
			# we've to add it back
			result.append(curr.value)
			return result			
		
		if curr.left and curr.left not in explored:
			explored[curr.left] = True
			queue.append([curr.left, dist + 1])
			
		if curr.right and curr.right not in explored:
			explored[curr.right] = True
			queue.append([curr.right, dist + 1])
			
		if parents[curr.value] and parents[curr.value] not in explored:
			explored[parents[curr.value]] = True
			queue.append([parents[curr.value], dist + 1])
	
	return []
	
def getNode(parents, root, target):
	if root.value == target:
		return root
	nodeParent = parents[target]
	if nodeParent.left is not None and nodeParent.left.value == target:
		return nodeParent.left
	return nodeParent.right
	
def createParents(root, parents, parent=None):
	if root:
		parents[root.value] = parent
		createParents(root.left, parents, root)
		createParents(root.right, parents, root)
