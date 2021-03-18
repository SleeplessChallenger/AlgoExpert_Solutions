# 1 Permutations
def getPermutations(arr):
	perms = []
	helper(0, arr, perms)
	return perms

def helper(idx, arr, perms):
	if idx == len(arr) - 1:
		perms.append(arr[:])
	else:
		for x in range(idx, len(arr)):
			swap(x, idx, arr)
			helper(idx + 1, arr, perms)
			swap(x, idx, arr)

def swap(idx1, idx2, arr):
	arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

# 2 Powerset
# a
def powerset(arr):
	cont = [[]]
	for x in arr:
		for y in range(len(arr)):
			temp = cont[y]
			cont.append(temp + [x])
	return cont

# b
def powerset(arr, idx=None):
	if idx is None:
		idx = len(arr) - 1
	if idx < 0:
		return [[]]
	ele = arr[idx]
	subs = powerset(arr, idx-1)
	for x in range(len(subs)):
		temp = subs[x]
		subs.append(temp + [ele])
	return subs

# 3 Phone Number Mnemonics
hashtable = {'1': ['1'], '2': ['a','b','c'], '3': ['d','e','f'],
			 '4': ['g','h','i'], '5': ['j','k','l'],
			 '6': ['m','n','o'], '7': ['p','q','r','s'],
			 '8': ['t','u','v'], '9': ['w','x','y','z'], '0': ['0']}

def phoneNumberMnemonics(phone):
	idx = 0
	curr =['0'] * len(phone)
	arr = []
	helper(idx, curr, arr, phone)
	return arr

def helper(idx, curr, arr, phone):
	if idx == len(phone):
		temp = ''.join(curr)
		arr.append(temp)
	else:
		digit = phone[idx]
		letters = hashtable[digit]
		for x in letters:
			curr[idx] = x
			helper(idx+1, curr, arr, phone)

# 4 Staircase traversal
# recursive with memoization
def staircaseTraversal(height, maxSteps):
	return func(height, maxSteps, {0: 1, 1:1})

def func(height, maxSteps, memo):
	if height in memo:
		return memo[height]
	# maxSteps points how many steps 
	# below we can go and sum their ways 
	# to receive number of ways for current
	# step
	curr = 0
	for x in range(1, min(height, maxSteps) + 1):
		curr += func(height - x, maxSteps, memo)

	memo[height] = curr
	return curr

# iterative with DP
def staircaseTraversal(height, maxSteps):
	arr = [0 for x in range(height + 1)]
	arr[0], arr[1] = 1, 1
	# + 1 in comprehension is because we
	# have base case with '0'

	for x in range(2, height + 1):
		step = 1
		# indicies in array represent ways (amount of ways)
		# via which we can reach this step
		while step <= x and step <= maxSteps:
		# <= maxSteps: because maxSteps show
		# how many layers below we can sum to
		# attain the current level
			arr[x] = arr[x] + arr[x - step]
			step += 1

	return arr[height]

# using Sliding window
def staircaseTraversal(height, maxSteps):
	arr = [1]
	curr = 0
	# ways to get to '0' is '1'

	for x in range(1, height + 1):
		start = x - maxSteps - 1
		# 'start' of the previous window
		# so as to subtract value that is
		# no longer in our window
		# '-1' here just enables to get the
		# value that we are to subtract
		end = x - 1
		# to take the previos value
		# that we need to add to 'curr'
		if start >= 0:
			curr -= arr[start]

		curr += arr[end]
		arr.append(curr)

	return arr[height] # curr also is OK
