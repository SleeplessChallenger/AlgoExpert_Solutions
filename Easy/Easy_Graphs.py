# 1 DFS
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, arr):
    	arr.append(self.name)
    	for x in self.children:
    		x.depthFirstSearch(arr)
    	return arr
