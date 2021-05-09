# 1 Max Subset Sum no adjacent
# a
def maxSubsetSumNoAdjacent(arr):
	if len(arr) == 0:
		return 0
	elif len(arr) == 1:
		return arr[0]
	total = arr[:]
	total[1] = max(total[0], total[1])
	for x in range(2, len(arr)):
		total[x] = max(total[x] + total[x-2], total[x-1])
	return total[-1]

# b
def maxSubsetSumNoAdjacent(arr):
	if len(arr) == 0:
		return 0
	elif len(arr) == 1:
		return arr[0]
	sec = arr[0]
	fir = max(arr[0], arr[1])
	for x in range(2, len(arr)):
		curr = max(arr[x] + sec, fir)
		sec = fir
		fir = curr
	return fir

# 2 Number of ways to make change
def numberOfWaysToMakeChange(n, denoms):
	arr = [0 for x in range(n + 1)]
	arr[0] = 1
	for x in denoms:
		for y in range(1, n + 1):
			if x <= y:
				arr[y] += arr[y - x]
				# arr[y] = arr[y] + arr[y - xか]
	return arr[n]

# 3 Min number of coins for change
def minNumberOfCoinsForChange(n, denoms):
	arr = [float('inf') for x in range(n + 1)]
	arr[0] = 0
	for x in denoms:
		for y in range(len(arr)):
			if x <= y:
				arr[y] = min(arr[y], arr[y - x] + 1)
	return arr[n] if arr[n] != float('inf') else -1

# 4 Number of ways to traverse graph
# mine 1
def func(width, height, memo={}):
	key = f'{width},{height}'
	if key in memo:
		return memp[key]
	if width == 1 and height == 1:
		return 1
	if width == 0 or height == 0:
		return 0
	memo[key] = func(width - 1, height, memo) + func(width, height - 1, memo)
	return memo[key]

# mine 2
def numberOfWaysToTraverseGraph(w, h, memo={}):
    key = f"{w},{h}"
	if key in memo:
		return memo[key]
	if w == 1 or h == 1:
		return 1
	memo[key] = numberOfWaysToTraverseGraph(w-1, h, memo) +\
				numberOfWaysToTraverseGraph(w, h-1, memo)
	
	return memo[key]

# mine 3
def numberOfWaysToTraverseGraph(w, h):
    arr = [[0 for x in range(w)] for y in range(h)]

	for up in range(w):
		for down in range(h):
			if up == 0 or down == 0:
				arr[down][up] = 1
			else:
				w_fig = arr[down][up-1]
				h_fig = arr[down-1][up]
				arr[down][up] = (w_fig + h_fig)

	return arr[h-1][w-1]

# a
def numberofWays(w, h):
	if w == 1 or h == 1:
		return 1
	return numberofWays(w - 1, h) + numberofWays(w, h - 1)

# b
def numberOfWaysToTraverseGraph(width, height):
	arr = [[0 for x in range(width + 1)] for y in range(height + 1)]
	for idx1 in range(1, width + 1):
		for idx2 in range(1, height + 1):
			if idx1 == 1 or idx2 == 1:
				arr[idx2][idx1] = 1
			else:
				left = arr[idx2][idx1 - 1]
				right = arr[idx2 - 1][idx1]
				arr[idx2][idx1] = (left + right)
	return arr[height][width]

# 5 Levenstein distance
# mine
def levenshteinDistance(str1, str2):
	arr = [[0 for x in range(1, len(str1)+1)] for y in range(1, len(str2)+1)]
	for x in range(1, len(str2)+1):
		arr[x][0] = x
	for y in range(1, len(str1)+1):
		arr[0][y] = y
	for idx1 in range(1, len(str2)+1):
		for idx2 in range(1, len(str1)+1):
			if str1[idx2-1] != str2[idx1-1]:
				arr[idx1][idx2] = 1 + min(arr[idx1-1][idx2-1], arr[idx1-1][idx2], arr[idx1][idx2-1])
			elif str1[idx2-1] == str2[idx1-1]:
				arr[idx1][idx2] = arr[idx1-1][idx2-1]
	return arr[-1][-1]

# not mine
def levenshteinDistance(str1, str2):
	arr = [[x for x in range(1, len(str1)+1)] for y in range(1, len(str2)+1)]
	# after this step we populate overall 2D array according to str1
	# and after following one we populate 2D array's first indices 
	# according to str2
	for x in range(1, len(str2)+1):
		arr[x][0] = arr[x-1][0] + 1
	for idx1 in range(1, len(str2)+1):
		for idx2 in range(1, len(str1)+1):
			if str2[idx1-1] == str1[idx2-1]:
				arr[idx1][idx2] = arr[idx1-1][idx2-1]
			elif str2[idx1-1] != str1[idx2-1]:
				arr[idx1][idx2] = 1 + min(arr[idx1-1][idx2], arr[idx1][idx2-1], arr[idx1-1][idx2-1])
	return arr[-1][-1]
