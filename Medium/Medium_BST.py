# 1 BST traversal
def inOrderTraverse(tree, arr):
    def traverse(tree):
		if tree.left:
			traverse(tree.left)
		arr.append(tree.value)
		if tree.right:
			traverse(tree.right)
	traverse(tree)
	return arr


def preOrderTraverse(tree, arr):
    def traverse(tree):
		arr.append(tree.value)
		if tree.left:
			traverse(tree.left)
		if tree.right:
			traverse(tree.right)
	traverse(tree)
	return arr
			


def postOrderTraverse(tree, arr):
    def traverse(tree):
		if tree.left:
			traverse(tree.left)
		if tree.right:
			traverse(tree.right)
		arr.append(tree.value)
	traverse(tree)
	return arr

# 2 Validate BST
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBST(tree):
	return helper(tree, float('-inf'), float('inf'))

def helper(tree, Min, Max):
	if tree is None:
		return True
	if tree.value < Min or tree.value >= Max:
		return False
	leftNode = helper(tree.left, Min, tree.value)
	return leftNode and helper(tree.right, tree.value, Max)

# 3 Min Height BST
# you can either use or not insert method

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def minHeightBST(arr):
	return helper(arr, 0, len(arr) - 1)

def helper(arr, left, right):
	if left > right:
		return None
	middle = (left + right) // 2
	node = BST(arr[middle])
	node.left = helper(arr, left, middle - 1)
	node.right = helper(arr, middle + 1, right)
	return node

# 4 BST construction
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
    	curr = self
    	while curr:
    		if curr.value > value:
    			if curr.left is None:
    				curr.left = BST(value)
    				break
    			curr = curr.left
    		elif curr.value < value:
    			if curr.right is None:
    				curr.right = BST(value)
    				break
    			curr = curr.right
    	return self

    def contains(self, value):
    	curr = self
    	while curr:
    		if curr.value > value:
    			curr = curr.left
    		elif curr.value < value:
    			curr = curr.right
    		else:
    			return True
    	return False

    def remove(self, value, parent=None):
    	curr = self
    	while curr:
    		if curr.value > value:
    			parent = curr
    			curr = curr.left
    		elif curr.value < value:
    			parent = curr
    			curr = curr.right
    		else:
    			if curr.left is not None and curr.right is not None:
    				curr.value = curr.right.minFind() # change itself happens here
    				curr.right.remove(curr.value, curr) # remove smallest from the right tree as we put it in the root
    			elif parent is None: # means we found the value instantly without if/elif + only one child
    				if curr.left is not None:
    					curr.value = curr.left.value
    					curr.right = curr.left.right
    					curr.left = curr.left.left # assign last as you'll need it
    				elif curr.right is not None:
    					curr.value = curr.right.value
    					curr.left = curr.right.left
    					curr.right = curr.right.right # assign last as you'll need it
    				else:
    					pass # no children
    			elif parent.left == curr:
				#  5
    				# /
    				#4 this to be removed
    				# \
    				#  3
    				parent.left = curr.left if curr.left is not None else curr.right
    			elif parent.right == cur:
    				parent.right = curr.left if curr.left is not None else curr.right
    			break
    	return self

   	def minFind():
   		curr = self
   		while curr:
   			if curr.left:
   				curr = curr.left
   		return curr.value

# 5 Find Kth largest value in BST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Time & Space O(n)
def findKthLargestValueInBst(tree, k):
    arr = []
    def traverse(node, arr):
        if node.left:
            traverse(node.left, arr)
        arr.append(node.value)
        if node.right:
            traverse(node.right, arr)
    traverse(tree, arr)
    return arr[-k]

# Time O(h + k) Space O(h)
class Help:
    def __init__(self, count, prev):
        self.count = count
        self.prev = prev


def findKthLargestValueInBst(tree, k):
    inst = Help(0, -1)
    traverse(tree, k, inst)
    return inst.prev

def traverse(node, k, inst):
    if not node or inst.count == k: # base case
        return

    traverse(node.right, k, inst)
    if inst.count < k:
    # if == then we return to initial function
        inst.count += 1
        inst.prev = node.value
        traverse(node.left, k, inst)
