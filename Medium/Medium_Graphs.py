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
