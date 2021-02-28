# 1 Invert Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# recursive
def invertBinaryTree(tree):
	if tree is None:
		return
	tree.left, tree.right = tree.right, tree.left
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

# iterative
def invertBinaryTree(tree):
	queue = [tree]
	while len(queue) != 0:
		node = queue.pop(0)
		if node is None:
			continue
		node.left, node.right = node.right, node.left
		queue += [node.left, node.right]