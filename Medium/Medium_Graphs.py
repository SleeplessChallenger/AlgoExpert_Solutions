# 1 Breadth-first search
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self


    def breadthFirstSearch(self, arr):
    	curr = self
    	queue = [curr]
    	explored = {}
    	explored[curr] = True
    	while len(queue) != 0:
    		node = queue.pop(0)
    		arr.append(node.name)
    		for x in node.children:
    			if x not in explored:
    				explored[x] = True
    				queue.append(x)
    	return arr

# 2 Single Cycle Check
def hasSingleCycle(arr):
	explored = 0
	curr = 0
	while len(arr) > explored:
		if explored > 0 and curr == 0:
			return False
		explored += 1
		curr = helper(arr, curr)
	return curr == 0

def helper(arr,curr):
	temp = arr[curr]
	return (temp + curr) % len(arr)
	# or if you write not in Python 
	# as modulo in Python works the following way:
	# -x % y == -(x % y) + y
	# to_return = (temp + curr) % len(arr)
	# return to_return if to_return >= 0 else to_return + len(arr)

# 3 River Sizes
def riverSizes(matrix):
    explored = [[False for x in row] for row in matrix]
    result = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if explored[x][y]:
                continue
            traverse(x,y,matrix,explored,result)
    return result

def traverse(idx1, idx2, matrix, explored, result):
    curr = 0
    stack = [[idx1,idx2]]
    while len(stack) != 0:
        curr_stack = stack.pop()
        i = curr_stack[0]
        j = curr_stack[1]
        if explored[i][j]: # nodes can twist in graph 
                           # hence we need this check
            continue
        explored[i][j] = True
        if matrix[i][j] == 0:
            continue
        curr += 1
        unexplored = helper(i, j, matrix, explored)
        for temp in unexplored:
            stack.append(temp)
    if curr > 0:
        result.append(curr)

def helper(i,j,matrix,explored):
    unvisitedNeigh = []
    if i > 0 and not explored[i-1][j]: # if not upmost row and above not visited
        unvisitedNeigh.append([i-1,j])
    if i < len(matrix) - 1 and not explored[i+1][j]: # if not downmost row and down not visited
        unvisitedNeigh.append([i+1,j])
    if j > 0 and not explored[i][j-1]:
        unvisitedNeigh.append([i,j-1])
    if j < len(matrix[i]) - 1 and not explored[i][j+1]:
        unvisitedNeigh.append([i,j+1])
    return unvisitedNeigh

# 4 Youngest common ancestor
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None
# mine
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # edge case if ancestor == one of the descendant
    if topAncestor == descendantOne or topAncestor == descendantTwo:
        return topAncestor

    # calculate depths of both descendants
    index1 = traverse(topAncestor, descendantOne)
    index2 = traverse(topAncestor, descendantTwo)

    # check if one of them is deeper
    # hence whether further actions are required
    node = equalTo(index1, index2, descendantOne, descendantTwo)
    return node

def traverse(top, desc):
    idx = 0
    while top != desc:
        idx += 1
        desc = desc.ancestor
    return idx

def equalTo(idx1, idx2, desc1, desc2):

    while idx1 != idx2:
        if idx1 > idx2:
            idx1 -= 1
            desc1 = desc1.ancestor
        elif idx2 > idx1:
            idx2 -= 1
            desc2 = desc2.ancestor

    while desc1 != desc2:
        desc1 = desc1.ancestor
        desc2 = desc2.ancestor

    return desc1

# not mine
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    index1 = traverse(topAncestor, descendantOne)
    index2 = traverse(topAncestor, descendantTwo)
    if index1 > index2:
        # higher means lower in my code
        backTrack(descendantOne, descendantTwo, index1 - index2)
    else:
        backTrack(descendantTwo, descendantOne, index2 - index1)

def traverse(top, desc):
    idx = 0
    while top != desc:
        idx += 1
        desc = desc.ancestor
    return idx

def backTrack(higher, lower, idx):
    # bring difference to 0
    while idx > 0:
        idx -= 1
        higher = higher.ancestor

    while higher != lower:
        higher = higher.ancestor
        lower = lower.ancestor
    return higher
