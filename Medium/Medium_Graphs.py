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
# mine
def hasSingleCycle(arr):
    if len(arr) <= 1:
		return True
	
	nums = [False for _ in arr]
	i = 0
	while not all(nums):
		i = helper(arr, i)
		if nums[i]:
			return False
		nums[i] = True
		
	return True
		
def helper(arr, i):
	new = arr[i] + i
	return new % len(arr)

# not mine
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

# 5 Cycle in Graph
# recursive with stack; T: O(v + e) S: O(v)
def cycleInGraph(edges):
    # has cycle -> True else False
    explored = [False for x in range(len(edges))]
    # for overall track
    stack = [False for x inr ange(len(edges))]
    # for currrent traversal track

    len_graph = len(edges)
    for edge in range(len_graph):
        if not explored[edge]:
            cycle = dfs(edges, edge, explored, stack)
            if cycle:
                return True
    return False

def dfs(edges, edge, explored, stack):
    stack[edge] = True
    explored[edge] = True

    for x in edges[edge]:
        if not explored[x]:
            cycle = dfs(edges, x, explored, stack)
            if cycle:
                return True
        elif stack[x]:
            return True
    stack[edge] = False
    return False

# recursive with colours; T: O(v + e) S: O(v)
white, grey, black = 0, 1, 2
# hence we can use them as variables
# white -> unvisited
# grey -> currently in stack
# black -> visited
def cycleInGraph(edges):
    colours = [white for x in range(len(edges))]
    len_edges = len(edges)

    for edge in range(len_edges):
        if colours[edge] != white:
        # if colours[edge] == black:
            continue
        cycle = dfs(edge, edges, colours)
        if cycle:
            return True
    return False

def dfs(edge, edges, colours):
    colours[edge] = grey

    for x in edges[edge]:
        if colours[x] == grey:
            return True
        elif colours[x] == black:
            continue
        elif colours[x] == white:
            cycle = dfs(x, edges, colours)
            if cycle:
                return True

    colours[edge] = False
    return False

# 6 Remove Islands
# recursive
def removeIslands(matrix):
    explored = [[False for x in rows] for rows in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowB = row == 0 or row == len(matrix) - 1
            colB = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowB or colB
            if not isBorder:
                continue
            if matrix[row][col] != 1:
                continue
            traverse(row, col, matrix, explored)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if explored[row][col]:
                continue
            matrix[row][col] = 0
    return matrix

def traverse(idx1, idx2, matrix, explored):
    stack = [(idx1, idx2)]
    while len(stack) != 0:
        curr_stack = stack.pop()
        node1, node2 = curr_stack

        if explored[node1][node2]:
            continue
        explored[node1][node2] = True

        neigh = explore(node1, node2, matrix)
        for edge in neigh:
            row, col = edge
            if matrix[row][col] != 1:
                continue

            stack.append(edge)

def explore(i, j, matrix):
    container = []

    if i - 1 >= 0: # UP
        container.append((i - 1, j))
    if j - 1 >= 0: # LEFT
        container.append((i, j - 1))
    if i + 1 <= len(matrix) - 1: # DOWN
        # or i + 1 <= len(matrix):
        container.append((i + 1, j))
    if j + 1 <= len(matrix[i]) - 1: # RIGHT
        # or j + 1 <= len(matrix[i]):
        container.append((i, j + 1))

    return container

# 7 Minimum Passses of Matrix
# mine
def minimumPassesOfMatrix(matrix):
    if len(matrix[0]) == 0:
    # `len(matrix) == 0` is also OK
        return 0
    elif len(matrix) == 1:
        return 0 if matrix[0][0] >= 0 else -1
    
    idx = 0
    arr = [[True if x > 0 else False for x in y] for y in matrix]
    
    while True:
        if main(matrix, arr) is True:
            idx += 1
        else:
            break
	# because eventually, even if we have
	# changed all to positive, there'll be
	# moment that no changes are made (everything)
	# is positive already => -1 will be an error
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                return -1
    return idx

def main(matrix, arr):
    count = 0
    temp = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                if helper(arr, i, j):
                    matrix[i][j] *= -1
                    temp.append([i, j])
                    count += 1
                else:
                    continue
            else:
                continue
    flip(temp, arr)
    
    return True if count != 0 else False

def helper(arr, i, j):
    if i > 0 and arr[i - 1][j] is True:
        return True
    if j > 0 and arr[i][j - 1] is True:
        return True
    if j < len(arr[0]) - 1 and arr[i][j + 1] is True:
        return True
    if i < len(arr) - 1 and arr[i + 1][j] is True:
        return True
    return False
    
def flip(temp, arr):
    while len(temp) != 0:
        nodes = temp.pop()
        a, b = nodes[0], nodes[1]
        arr[a][b] = True

# not mine
def minimumPassesOfMatrix(matrix):
    positive_idx = getPositive(matrix)
    count = main(positive_idx, matrix)
    return count - 1 if noNegative(matrix) else -1

    
def main(pos, matrix):
    count = 0
    
    while len(pos) != 0:
        new = pos
        pos = []
        
        while len(new) != 0:
            row, col = new.pop(0)
            
            adjacent = getAdjacent(row, col, matrix)
            
            for ele in adjacent:
                r, c = ele
                
                if matrix[r][c] < 0:
                    matrix[r][c] *= -1
                    pos.append([r, c])
        count += 1
    return count
                    
def getPositive(matrix):
    result = []
    
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] > 0:
                result.append([x, y])
    return result

def noNegative(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] < 0:
                return False
    return True

def getAdjacent(i, j, matrix):
    temp = []
    
    if i > 0:
        temp.append([i - 1, j])
    if j > 0:
        temp.append([i, j - 1])
    if i < len(matrix) - 1:
        temp.append([i + 1, j])
    if j < len(matrix[i]) - 1:
        temp.append([i, j + 1])
    return temp
