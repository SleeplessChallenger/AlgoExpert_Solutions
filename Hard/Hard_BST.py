# 1 Same BSTs
def sameBsts(arrayOne, arrayTwo):
	if len(arrayOne) != len(arrayTwo):
		return False
	
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	
	if arrayOne[0] != arrayTwo[0]:
		return False

	sm1, sm2, big1, big2 = getValue(arrayOne, arrayTwo)
	
	return sameBsts(sm1, sm2) and sameBsts(big1, big2)

def getValue(arr1, arr2):
	smaller1 = []
	smaller2 = []
	bigger1 = []
	bigger2 = []
	
	for value in range(1, len(arr1)):
		if arr1[value] >= arr1[0]:
			bigger1.append(arr1[value])
		elif arr1[value] < arr1[0]:
			smaller1.append(arr1[value])
	
	for value in range(1, len(arr2)):
		if arr2[value] >= arr2[0]:
			bigger2.append(arr2[value])
		elif arr2[value] < arr2[0]:
			smaller2.append(arr2[value])
	
	return smaller1, smaller2, bigger1, bigger2

# 2 Validate Three Nodes
# mine
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    result = helper(nodeOne, nodeTwo, nodeThree)
	if result is False:
		return False

	# if we found that descendant is 'third', then
	# ancestor of nodeTwo must be nodeOne
	# else nodeThree
	checkNode = nodeThree if result == 'first' else nodeOne
	return check(checkNode, nodeTwo)

	
def helper(nodeOne, nodeTwo, nodeThree):
	if nodeTwo is None:
		return False
	if nodeTwo == nodeOne:
		return 'first'
	if nodeTwo == nodeThree:
		return 'third'

	left = helper(nodeOne, nodeTwo.left, nodeThree)
	right = helper(nodeOne, nodeTwo.right, nodeThree)
	
	if not left and not right:
		return False
	elif left == 'first' or right == 'first':
		return 'first'
	else:
		return 'third'

def check(checkNode, nodeTwo):
	if checkNode is None:
		return False
	if checkNode == nodeTwo:
		return True
	
	left = check(checkNode.left, nodeTwo)
	right = check(checkNode.right, nodeTwo)
	
	return False if not left and not right else True

# not mine
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# recursive T: O(h) S: O(h)
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDesc(nodeTwo, nodeOne):
		return isDesc(nodeThree, nodeTwo)
	
	if isDesc(nodeTwo, nodeThree):
		return isDesc(nodeOne, nodeTwo)
	
	return False

def isDesc(mainNode, goal):
	if mainNode is None:
		return False
	if mainNode == goal:
		return True
	
	return isDesc(mainNode.left, goal) if mainNode.value > goal.value \
		   else isDesc(mainNode.right, goal)

# iterative T: O(h) S: O(1)
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
	if isDesc(nodeTwo, nodeOne):
		return isDesc(nodeThree, nodeTwo)
	
	if isDesc(nodeTwo, nodeThree):
		return isDesc(nodeOne, nodeTwo)
	
	return False

def isDesc(node, goal):
	root = node
	while root:
		if root == goal:
			return True
		if root.value > goal.value:
			root = root.left
		else:
			root = root.right
	
	return False

# T: O(d) S: O(1)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    searchOne = nodeOne
	searchTwo = nodeThree
	
	while True:
		oneFromThree = searchTwo == nodeOne
		threeFromOne = searchOne == nodeThree
		foundTwo = searchOne == nodeTwo or searchTwo == nodeTwo
		noNodes = searchOne is None and searchTwo is None
		if oneFromThree or threeFromOne or foundTwo or noNodes:
			break
		
		if searchOne:
			searchOne = searchOne.left if searchOne.value > nodeTwo.value \
									   else searchOne.right
		if searchTwo:
			searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value \
									   else searchTwo.right
	
	foundEachOther = searchOne == nodeThree or searchTwo == nodeOne
	foundTwo = searchOne == nodeTwo or searchTwo == nodeTwo
	if not foundTwo or foundEachOther:
		return False
	
	# if ancestor of nodeTwo is nodeThree ->
	# search from nodeTwo for nodeOne &
	# vice versa
	return checkValues(nodeTwo, nodeThree if searchOne == nodeTwo else nodeOne)

def checkValues(node, goal):
	while node:
		if node is goal:
			return True
		node = node.left if node.value > goal.value else node.right
	
	return False
