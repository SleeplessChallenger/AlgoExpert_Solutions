# 1 Number of Binary Tree Topologies

# recursive
# see papers for detailed explanation
# of every recursive call
def numberOfBinaryTreeTopologies(n, memo={0: 1}):
    if n in memo:
		return memo[n]
	count = 0
	# if without reversed, then at first:
	# 0: leftSubtree 2: rightSubtree
	# else: 2: leftSubtree 0: rightSubtree
	for left in reversed(range(n)):
		right = n - 1 - left
		leftSubtree = numberOfBinaryTreeTopologies(left, memo)
		rightSubtree = numberOfBinaryTreeTopologies(right, memo)
		count += leftSubtree * rightSubtree
	memo[n] = count
	return count

# iterative
def numberOfBinaryTreeTopologies(n):
    cache = [1]
	for num in range(1, n + 1):
		numberOfTrees = 0
		for leftTree in range(0, num):
			leftSubtree = cache[leftTree]
			rightTree = num - 1 - leftTree
			# use `num` as we need max
			# possible amount of branches
			rightSubtree = cache[rightTree]
			numberOfTrees += leftSubtree * rightSubtree
		cache.append(numberOfTrees)
	return cache[n]
