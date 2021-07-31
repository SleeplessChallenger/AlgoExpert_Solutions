# 1 Knuth-Morris-Pratt Algorithm
def knuthMorrisPrattAlgorithm(string, substring):
	pattern = buildPattern(substring)
	return findResult(string, substring, pattern)

def buildPattern(substring):
	i = 1
	j = 0
	arr = [-1 for _ in range(len(substring))]
	
	while i < len(substring):
		if substring[i] == substring[j]:
			arr[i] = j
			i += 1
			j += 1
		elif j > 0:
			j = arr[j - 1] + 1
			# if there is pattern -> take it & + 1
			# elif no: -1 + 1
		else:
			i += 1
	return arr

def findResult(string, sub, pat):
	i = 0
	j = 0
	
	while i + len(sub) - j <= len(string):	
		# if j == len(sub):
			# return True
		if string[i] == sub[j]:
			if j == len(sub) - 1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pat[j - 1] + 1
		else:
			i += 1
	return False

# 2 A* Algorithm

#  explanation
# Edge cases to keep in mind:
# 	1. Are starting & ending positions valid?
# 	2. Can start & end positions be on the same level?
# 	3. Can start & end position be an obstacle?

# Use "heuristic", i.e. guess, to figure out how far is
# certain node from the end node? So, before visitng any node
# 2 things that we'll consider are: a) how long does it take
# us to get to current node? b) how long do we think it'll
# take us to reach end node? The better heuristic ->
# the fewer wrong nodes we'll visit.
# So, 3 factors to bear in mind before visiting any node:
# 	HGF where H - heuristic value, i.e. how long is 
# 	H node from end node? G - shortest path from start
# 	node to the given node. F: G + H, so we're looking
# 	for node with lowest F-score.

# Start by giving every `start` node all three values (HGF).
# * Which heuristic to use? -> Here we'll use Manhattan distance
# 	Ex: (end pos - curr pos) -> (4 - 0) + (3 - 1) = 6 => H = 6.
# 	Or we can simply calc. cells in conceptual overview.
# 	(formula above is representation of the method)
# 	F = G + H => 0 + 6 = 6
# 	And it's really a distance from our `start` node to `end` node.
# 	PS: Manhattan distance is the typical one to use when
# 		we can move only in 4 directions (no diagonals).
# 		If diagonals are possible: Euclidean distance.
# H: 4 - 1 = 3; 3 - 4 = -1; 2  
			
# So, start node: G - 0, H - 6, F - 6. One to the right:
# G - 1, H - 5: (4 - 0) + (3 - 2) = 5, F = 5 + 1 = 6.
# One to the left: G - 1, H - 7: (4 - 0) + (3 - 0), F = 1 + 7 = 8

# Then, take the one with smallest F (it'll be the node to the right).
# From that node we can go to the left and to the right. If we go
# to the left, we'll try to update G, but see that curr G score
# is lower than the one we're trying to put => don't go in this
# direction.
# Note: the one to the left from the very beginning will be seen
# after we reached the rightmost of the first row. As these two
# cells will have the same H score - 8. Order of cells with
# equal H score can be done by picking ones with lower G score
# at first.

# Every time we add/update G score of the node, we also keep
# track of the node we've come from (or we update node we came
# from in case this node aldready has some).
# So, after we reached end node, we do some kind of backtracking
# and when we found that node has no prev. node -> start node,
# such modus operandi will give the whole path.

# Also, G score of every next node is G score of prev. node + 1.
# We update G score ONLY if it's smaller than current G score,
# and in such case we also update the node we came from for this
# node (look above in the previous paragraph)

class Graph:
	def __init__(self, row, col, value):
		self.id = f"{row}:{col}"
		self.row = row
		self.col = col
		self.value = value
		self.distFromStart = float('inf') # G
		self.distToEnd = float('inf') # F
		# F = self.distFromStart + heuristic value
		self.cameFrom = None


def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    matrix = initGraph(graph)
	
	startNode = matrix[startRow][startCol]
	endNode = matrix[endRow][endCol]
	
	startNode.distFromStart = 0
	startNode.distToEnd = startNode.distFromStart +\
		manhattanDistance(startNode, endNode)
	
	nodesToVisit = PriorityQueue([startNode])
	
	while nodesToVisit.isEmpty() is not True:
		# take node with curr. smallest G score
		currNode = nodesToVisit.remove()
		
		if currNode == endNode:
			break
		
		adjacentNodes = getAdjacentNodes(currNode, matrix)
		
		for node in adjacentNodes:
			if node.value == 1:
				continue
			
			tempDist = currNode.distFromStart + 1
			# as next node's G is currNode's G + 1
			
			if tempDist >= node.distFromStart:
			# if G of next node is smaller than
			# the one from currNode + 1 =>
			# there is another path that takes
			# smaller steps, hence we skip
				continue
			
			node.cameFrom = currNode
			node.distFromStart = tempDist # G
			node.distToEnd = tempDist + manhattanDistance(
				node, endNode) # func: H; .distToEnd: F
			
			if nodesToVisit.containsNode(node):
				nodesToVisit.update(node)
			else:
				nodesToVisit.insert(node)
			
	return backtrackNodes(endNode)		
	
def getAdjacentNodes(node, allNodes):	
	adjacent = []
	
	numRows = len(allNodes)
	numCols = len(allNodes[0])

	row = node.row
	col = node.col
	
	if row < numRows - 1:
		adjacent.append(allNodes[row + 1][col])
		
	if row > 0:
		adjacent.append(allNodes[row - 1][col])
		
	if col < numCols - 1:
		adjacent.append(allNodes[row][col + 1])
		
	if col > 0:
		adjacent.append(allNodes[row][col - 1])
		
	return adjacent
	
def manhattanDistance(currNode, endNode):
	currRow = currNode.row
	currCol = currNode.col
	endRow = endNode.row
	endCol = endNode.col
	
	return abs(endRow - currRow) + abs(endCol - currCol)

def initGraph(graph):
	nodes = []
	
	for idx in range(len(graph)):
		nodes.append([])
		row = graph[idx]
		for idx2 in range(len(row)):
			nodes[idx].append(Graph(idx, idx2, row[idx2]))
			# row, col, value (0 or 1)

	return nodes

def backtrackNodes(node):
	if node.cameFrom is None:
		return []
	
	curr = node
	result = []
	
	while curr:
		result.append([curr.row, curr.col])
		curr = curr.cameFrom
	
	# return list(reversed(result))
	return result[::-1]

	
class PriorityQueue:
	def __init__(self, arr):
		self.nodePositionInQueue = {arr[idx].id: idx for idx in range(len(arr))}
		# self.nodePositionInQueue = {node.id: idx for idx, node in enumerate(arr)}
		# as every item in `arr` is class object with
		# it's own properties, we'll use `.` notation
		# to pick up the required ones
		self.heap = self.buildHeap(arr)
	
	def buildHeap(self, heap):
		firstParent = (len(heap) - 1) // 2
		for idx in reversed(range(firstParent + 1)):
			self.siftDown(idx, len(heap) - 1, heap)
		
		return heap
	
	def isEmpty(self):
		return len(self.heap) == 0
	
	def remove(self):
		# we need to do  here
		# with `swap` as we not only
		# change values, but `id` as well
		if self.isEmpty():
			return
		
		self.swap(0, len(self.heap) -1)
		drop = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		del self.nodePositionInQueue[drop.id]
		return drop
	
	def insert(self, node):
		self.heap.append(node)
		self.nodePositionInQueue[node.id] = len(self.heap) - 1
		self.siftUp(len(self.heap) - 1, self.heap)
	
	def swap(self, i, j):
		self.nodePositionInQueue[self.heap[i].id] = j
		self.nodePositionInQueue[self.heap[j].id] = i
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
	
	def containsNode(self, node):
		return node.id in self.nodePositionInQueue
	
	def update(self, node):
		self.siftUp(self.nodePositionInQueue[node.id], self.heap)
		
	def siftUp(self, currIdx, heap):
		parentIdx = (currIdx - 1) // 2
		while currIdx > 0 and heap[currIdx].distToEnd < heap[parentIdx].distToEnd:
			self.swap(currIdx, parentIdx)
			currIdx = parentIdx
			parentIdx = (currIdx - 1) // 2
	
	def siftDown(self, currIdx, length, heap):
		idxOne = currIdx * 2 + 1
		while idxOne <= length:
			idxTwo = currIdx * 2 + 2 if currIdx * 2 + 2 <= length else -1
			if idxTwo != -1 and heap[idxTwo].distToEnd < heap[idxOne].distToEnd:
				swap = idxTwo
			else:
				swap = idxOne
			
			if heap[swap].distToEnd < heap[currIdx].distToEnd:
				self.swap(currIdx, swap)
				currIdx = swap
				idxOne = currIdx * 2 + 1
			else:
				return
