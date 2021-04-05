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
	# cases to deal with
	# 1. if both childs are in place
	# 2. if no parent (find at first try) + only one child (when both above is dealth with)
	# 3. if parent exists, but only 1 child
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

# 6 Reconstruct BST
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# first: T: O(n^2); S: O(n)
def reconstructBst(arr):
    if len(arr) == 0:
        return None

    curr = arr[0]
    rightTree = len(arr)

    # traverse till curr < 'some value' in array
    # if so, change right border for the index
    # of that 'some value'

    for x in range(1, len(arr)):
        if arr[x] >= curr:
            rightTree = x
            break

    # from next after arr[0] on current step
    leftNode = reconstructBst(arr[1:rightTree])
    # if there is value > curr => 1) rightTree = len(arr) [suppose 4]
    # if last in this arr > than curr => 2) rightTree = 3
    rightNode = reconstructBst(arr[rightTree:])
    return BST(curr, leftNode, rightNode)

# second: T: O(n); S: O(n)
class Help:
    def __init__(self, idx):
        self.idx = idx


def reconstructBst(values):
    inst = Help(0)
    return func(values, inst, float('-inf'), float('+inf'))

def func(arr, inst, lower, upper):
    if inst.idx == len(arr):
        return None
    # if .idx == len(arr) -> done

    # .idx means what value from arr 
    # we'll take on the current recursive call
    curr = arr[inst.idx]
    if curr < lower or curr >= upper:
        return None

    inst.idx += 1
    leftNode = func(arr, inst, lower, curr)
    rightNode = func(arr, inst, curr, upper)
    return BST(curr, leftNode, rightNode)
