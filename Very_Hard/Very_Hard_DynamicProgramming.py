# 1 Max Profit With K Transactions

# first
# Time: O(n*k) Space: O(n*k)
def maxProfitWithKTransactions(prices, k):
	if len(prices) == 0:
		return 0
    profits = [[0 for _ in prices] for _ in range(k + 1)]
	
	for transaction in range(1, k + 1):
		maxFigure = float('-inf')
		for price in range(1, len(prices)):
			# to bypass n^2 time we keep only
			# biggest amount of previous price
			# when going through one 'transaction level'
			maxFigure = max(maxFigure, - prices[price - 1]
							+ profits[transaction - 1][price - 1])

			profits[transaction][price] = max(
				profits[transaction][price - 1],
				prices[price] + maxFigure)
	
	return profits[-1][-1]

# second
# Time: O(n*k) Space: O(n)
def maxProfitWithKTransactions(prices, k):
    if len(prices) == 0:
		return 0
	even = [0 for _ in prices]
	odd = [0 for _ in prices]
	
	for tr in range(1, k + 1):
		maxPr = float('-inf')
		if tr % 2 == 0:
			curr = even
			prev = odd
		else:
			curr = odd
			prev = even
		for p in range(1, len(prices)):
			maxPr = max(maxPr, - prices[p - 1] + prev[p - 1])
			curr[p] = max(curr[p - 1], prices[p] + maxPr)
	
	return even[-1] if k % 2 == 0 else odd[-1]

# 2 Palindrome Partitioning Min Cuts
# T: O(n^3) S: O(n^2)
def palindromePartitioningMinCuts(string):
	arr = [[False for _ in string] for _ in string]
	
	# gist is in array construction.
	# If we have substring `abba` then it'll
	# resulted as True as a = a and in
	# the same loop b = b. But if we have
	# `apba` then here a = a, but p != b
	# hence no substring
	for i in range(0, len(string)):
		# `i` is start index (row)
		for j in range(i, len(string)):
			# `j` is end index (col)
			arr[i][j] = helper(string[i:j + 1])

	# `results` will depict min number of cuts
	# needed for every substring which started
	# at idx = 0 and up to the particular index
	result = [float('inf') for _ in string]
	# below will be our `end` (`i`) which then
	# will be chased by start (`j` index)
	for i in range(len(string)):
		if arr[0][i]:
			result[i] = 0
		else:
			result[i] = result[i - 1] + 1
			for j in range(1, i):
				# we move our start (row) to
				# our end (column) to find palindromes
				if arr[j][i] and result[j - 1] + 1 < result[i]:
					result[i] = result[j - 1] + 1
	# pb
	# [False, False, False, False, True, False, False, False, False]
	# bb
	# [False, False, False, False, True, False, False, True, False]
	return result[-1]

def helper(string):
	i, j = 0, len(string) - 1
	while i < j:
		if string[i] != string[j]:
			return False
		i += 1
		j -= 1
	# here when `i` overlaps `j`
	return True

#  3 Longest Increasing Subsequence
def longestIncreasingSubsequence(arr):
    if len(arr) <= 1:
		return arr
	# we care about longest distance
	refs = [None for _ in arr]
	dist = [1 for _ in arr]
	# `1` because longest can be
	# considered the value itself
	longestLastIdx = 0
	
	for i in range(1, len(arr)):
		curr = arr[i]
		for j in range(0, i):
			prev = arr[j]
			if curr > prev and dist[j] + 1 > dist[i]:
				dist[i] = dist[j] + 1
				refs[i] = j
		
		if dist[longestLastIdx] < dist[i]:
			longestLastIdx = i
	
	return getValues(longestLastIdx, refs, arr)

def getValues(idx, refs, arr):
	result = []
	
	while idx is not None:
		result.append(arr[idx])
		idx = refs[idx]
		
	return list(reversed(result))

# 4 Longest String Chain
# with nested hash table
def longestStringChain(strings):
    ht = {}
	createHashTable(ht, strings)
	# we need `key` to sort by length
	strings.sort(key=len)

	for string in strings:
		findLongest(string, ht)
	
	elements = getLongest(ht, strings)
	return elements if len(elements) > 1 else []
	
def findLongest(string, ht):
	for idx in range(len(string)):
		curr = getString(string, idx)
		if curr not in ht:
			continue
		else:
			count = ht[curr]['length']
			# `+ 1` below as we need
			# to include the value we'd
			# like to attach to
			if count + 1 >= ht[string]['length']:
				ht[string]['length'] = ht[curr]['length'] + 1
				ht[string]['next'] = curr

def getLongest(ht, strings):
	result = 0
	strRes= ""
	for string in strings:
		if ht[string]['length'] > result:
			result = ht[string]['length']
			strRes = string

	allChain = []
	
	while strRes != "":
		allChain.append(strRes)
		strRes = ht[strRes]['next']
	
	return allChain
	
def getString(string, idx):
	# exclusive to the idx and from the
	# next element
	return string[0:idx] + string[idx+1:]
	
	
def createHashTable(ht, strings):
	# we need dict() as with
	# tuple/list we then cannot
	# iterate and build chain of strings
	for string in strings:
		ht[string] = {'next': "", 'length': 1}

# with nested array
def longestStringChain(strings):
    ht = {}
	createHashTable(ht, strings)
	# we need `key` to sort by length
	strings.sort(key=len)

	for string in strings:
		findLongest(string, ht)
	
	elements = getLongest(ht, strings)
	return elements if len(elements) > 1 else []
	
def findLongest(string, ht):
	for idx in range(len(string)):
		curr = getString(string, idx)
		if curr not in ht:
			continue
		else:
			count = ht[curr][1]
			# `+ 1` below as we need
			# to include the value we'd
			# like to attach to
			if count + 1 >= ht[string][1]:
				ht[string][1] = ht[curr][1] + 1
				ht[string][0] = curr

def getLongest(ht, strings):
	result = 0
	strRes= ""
	for string in strings:
		if ht[string][1] > result:
			result = ht[string][1]
			strRes = string

	allChain = []
	
	# !! `for` cannot be used
	# as it'll iterate over letters,
	# not words
	while strRes != "":
		allChain.append(strRes)
		strRes = ht[strRes][0]
	
	return allChain
	
def getString(string, idx):
	# exclusive to the idx and from the
	# next element
	return string[0:idx] + string[idx+1:]
	
	
def createHashTable(ht, strings):
	# we can use either `dict`
	# or `list`
	for string in strings:
		ht[string] = ["", 1]

# 5 Square of Zeros
# Time: O(n^4) Space: O(1)
def squareOfZeroes(matrix):
    length = len(matrix)
	for row in range(length):
		for col in range(length):
			# as we need at least 2*2
			limit = 2
			# to exclude rightmost col
			# and bottom-most row, as we
			# treat every cell as top
			# left corner, & to grow our
			# border we use this while loop
			while limit <= length - row\
			and limit <= length - col:
				bottomRow = row + limit - 1
				rightBorder = col + limit - 1
				# to start from 2*2 square 
				# we subtract 1
				if isSquare(matrix, row, col,
							bottomRow, rightBorder):
					return True
				limit += 1
			
	return False
	
def isSquare(m, r, c, bR, rB):
	# `+ 1` as we need to check
	# every cell in the border
	for i in range(r, bR + 1):
		if m[i][c] != 0 or m[i][rB]:
			return False
	
	for j in range(c, rB + 1):
		if m[r][j] != 0 or m[bR][j] != 0:
			return False
	
	return True
