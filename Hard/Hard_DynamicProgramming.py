# 1 Longest Common Subsequence
# first  T: O(nm * min(n,m)) S: O(nm * min(n,m))
def longestCommonSubsequence(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
		return []
	
	arr = [[ [] for x in range(len(str1) + 1)]
		  	    for y in range(len(str2) + 1)]
	
	for up in range(1, len(str2) + 1):
		for down in range(1, len(str1) + 1):
			if str1[down - 1] == str2[up - 1]:
				arr[up][down] = arr[up-1][down-1] + [str1[down-1]]
			else:
				upper = arr[up-1][down]
				left = arr[up][down-1]
				arr[up][down] = upper if len(upper) > len(left) else left
	
	return arr[-1][-1]

# second T: O(nm) S: O(nm)
def longestCommonSubsequence(str1, str2):
    arr = [[ [None, 0, None, None] for x in range(len(str1) + 1)]
		  						   for y in range(len(str2) + 1)]
	
	for up in range(1, len(str2) + 1):
		for down in range(1, len(str1) + 1):
			if str1[down - 1] == str2[up - 1]:
				arr[up][down] = [str1[down-1], arr[up-1][down-1][1]+1,
								 up-1, down-1]
			else:
				if arr[up-1][down][1] > arr[up][down-1][1]:
					arr[up][down] = [None, arr[up-1][down][1],
									 up-1, down]
				else:
					arr[up][down] = [None, arr[up][down][1],
									 up, down-1]
	return helper(arr)

def helper(arr):
	result = []
	i = len(arr) - 1
	j = len(arr[0]) - 1
	
	while i != 0 and j != 0:
		curr = arr[i][j]
		if curr[0] is not None:
			result.append(curr[0])
		i = curr[2]
		j = curr[3]
	return list(reversed(result))

# 2 Knapsack Problem
def knapsackProblem(items, capacity):
    arr = [[0 for x in range(capacity + 1)]\
		      for y in range(len(items) + 1)]
	print(arr)
	for up in range(1, len(items) + 1):
		curr_weight = items[up - 1][1]
		curr_value = items[up - 1][0]
		
		for down in range(0, capacity + 1):
			if down >= curr_weight:
				arr[up][down] = max(arr[up-1][down],\
								    arr[up-1][down - curr_weight] + curr_value)
			else:
				arr[up][down] = arr[up-1][down]
	return [arr[-1][-1], helper(arr, items)]

def helper(arr, items):
	row = len(arr) - 1
	col = len(arr[0]) - 1
	result = []
	
	while row > 0:
		if arr[row][col] == arr[row-1][col]:
			row -= 1
		else:
			result.append(row-1)
			# (above) row - 1 as
			# we need to shift everything
			# by 1 due to additional row
			col -= items[row-1][1]
			row -= 1
		if col == 0:
			break
	return list(reversed(result))

# 3 Max Sum Increasing Subsequence
def maxSumIncreasingSubsequence(arr):
    sums = [x for x in arr]
	ref = [None for x in arr]
	
	sums[0] = arr[0]
	maxIdx = 0
	
	for i in range(1, len(arr)):
		curr = arr[i]
		for j in range(0, i):
			prev = arr[j]
			if prev < curr and sums[i] < sums[j] + curr:
				# second part of `if statement` is
				# vital as without it unnecessary
				# indicies would be added to ref
				sums[i] = (sums[j] + curr)
				ref[i] = j
	
		if sums[maxIdx] < sums[i]:
			maxIdx = i
	
	return [sums[maxIdx], backTrack(ref, maxIdx, arr)]

def backTrack(ref, idx, arr):
	result = []
	
	while idx is not None:
		result.append(arr[idx])
		idx = ref[idx]
	
	return list(reversed(result))

# 4 Min Number of Jumps

# T: O(n^2) S: O(n)
def minNumberOfJumps(array):	
	jumps = [float('inf') for _ in array]
	jumps[0] = 0
	
	for i in range(1, len(array)):
		for j in range(0, i):
			if array[j] + j >= i:
				# we take value(number of jumps) itself
				# and add the `range` within
				# which it can spread
				jumps[i] = min(jumps[i], jumps[j] + 1)
				# `+1` because we know from previous
				# that we're able to reach `i`, hence
				# we're to make jump from [j]. And this
				# jump will be represented by `+1`
	return jumps[-1]

# T: O(n) S: O(1)
def minNumberOfJumps(arr):
	if len(arr) == 1:
		return 0
	
    max_reach = arr[0]
	jumps = 0
	steps = arr[0]
	
	for i in range(1, len(arr) - 1):
		# `-1` because when we're at a final
		# index, we don't need to use it
		max_reach = max(max_reach, arr[i] + i)
		steps -= 1
		if steps == 0:
			jumps += 1
			steps = max_reach - i
	# as we don't iterate till last index
	# we need one more jump to reach final
	return jumps + 1

# 5 Water Area
# mine
def waterArea(heights):
	if len(heights) < 3 or sum(heights) < 2:
		return 0
	
    nestedHeight = []
	result = []
	
	for x in range(len(heights)):
		helper(x, heights, nestedHeight)
		small = min(nestedHeight[x])
		result.append(small - heights[x])

	return sum([x for x in result if x > 0])
	
	
def helper(idx, heights, nestedHeight):
	l_idx = idx - 1
	r_idx = idx + 1
	
	left = float('-inf') if l_idx >= 0 else 0
	right = float('-inf') if r_idx <= len(heights) - 1 else 0
	
	while l_idx >= 0:
		left = max(heights[l_idx], left)
		l_idx -= 1
	
	while r_idx <= len(heights) - 1:
		right = max(heights[r_idx], right)
		r_idx += 1
	
	nestedHeight.append([left, right])
	return

# not mine
def waterArea(heights):
    result = [0 for x in heights]
	leftMax = 0
	
	for x in range(len(heights)):
		h = heights[x]
		result[x] = leftMax
		leftMax = max(leftMax, h)
	print(result)
	rightMax = 0
	for x in reversed(range(len(heights))):
		h = heights[x]
		minHeight = min(rightMax, result[x])
		# (above) we choose min(left, right)
		if h < minHeight:
			# find distance to the tallest pillar
			result[x] = minHeight - h
		else:
			result[x] = 0
		rightMax = max(rightMax, h)
	
	return sum(result)


# 6 Disk Stacking
def diskStacking(disks):
	disks.sort(key=lambda x: x[2])
	
	sums = [disks[x][2] for x in range(len(disks))]
	ref = [None for x in disks]
	
	for i in range(len(disks)):
		curr = disks[i]
		for j in range(0, i):
			prev = disks[j]
			if curr[0] > prev[0] and curr[1] > prev[1] and curr[2] > prev[2]:
				if sums[i] < sums[j] + curr[2]:
					sums[i] = (curr[2] + sums[j])
					ref[i] = j
	
	value = max(sums)
	idx = sums.index(value)
	
	return backTrack(idx, ref, disks)

def backTrack(idx, ref, disks):
	result = []
	
	while idx is not None:
		result.append(disks[idx])
		idx = ref[idx]
	
	return list(reversed(result))

# 7 Numbers in PI
def numbersInPi(pi, numbers):
	ht = {x: True for x in numbers}
	result = helper(pi, ht, {}, 0)
	return result if result != float('inf') else -1

def helper(pi, ht, cache, idx):
	if idx == len(pi):
		return -1
	
	if idx in cache:
		return cache[idx]
	
	fig = float('inf')
	for i in range(idx, len(pi)):
		chunk = pi[idx:i + 1]
		if chunk in ht:
			temp = helper(pi, ht, cache, i + 1)
			fig = min(fig, temp + 1)
	
	cache[idx] = fig
	return cache[idx]
