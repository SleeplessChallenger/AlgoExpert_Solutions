# 1 Subarray sort
def subarraySort(arr):
	left = float('inf')
	right = float('-inf')

	for idx in range(len(arr)):
		if helper(idx, arr[idx], arr):
			left = min(left, arr[idx])
			right = max(right, arr[idx])

	if left == float('inf'):
		return [-1, -1]

	idxLeft = 0
	while arr[idxLeft] <= left:
		idxLeft += 1

	idxRight = len(arr) - 1
	while arr[idxRight] >= right:
		idxRight -= 1

	return [idxLeft, idxRight]

def helper(idx, figure, arr):
	if idx == 0:
		return arr[idx + 1] < figure
	elif idx == len(arr) - 1:
		return arr[idx - 1] > figure
	return arr[idx - 1] > figure or arr[idx + 1] < figure

# 2 Largest Range
def largestRange(array):
	ht = {}
	longest = 0
	result = []

	for x in array:
		ht[x] = True

	for x in array:
		if ht[x] is False:
			continue
		ht[x] = False
		left = x - 1
		right = x + 1
		current = 1

		while left in ht:
			ht[left] = False
			left = left - 1
			current += 1

		while right in ht:
			ht[right] = False
			right = right + 1
			current += 1

		if longest < current:
			longest = current
			result = [left + 1, right - 1]

	return result

# 2
def minRewards(scores):
	rewards = [1 for x in scores]
	localMins = getLocals(scores)
	for local in localMins:
		explore(local, scores, rewards)
	return sum(rewards)

def getLocals(scores):
	if len(scores) == 1:
		return [0]
	cont = []
	for idx in range(len(scores)):
		if idx == 0 and scores[idx] < scores[idx+1]:
			cont.append(idx)
		if idx == len(scores) - 1 and scores[idx] < scores[idx-1]:
			cont.append(idx)
		if idx == 0 or idx == len(scores) - 1:
			continue
		if scores[idx] < scores[idx-1] and scores[idx] > scores[idx+1]:
			cont.append(idx)
	return cont

def explore(local, scores, rewards):
	leftIdx = local - 1
	rightIdx = local + 1

	while leftIdx >= 0 and scores[leftIdx] < scores[leftIdx+1]:
		rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx+1]+1)
		leftIdx -= 1

	while rightIdx <= len(scores) - 1 and scores[rightIdx] > scores[rightIdx-1]:
		rewards[rightIdx] = rewards[rightIdx-1] + 1
		# because when to 'right' we assign only once
		# but when to 'left' then we may reassign rewards existing
		rightIdx += 1

# 3
def minRewards(scores):
	rewards = [1 for x in scores]

	for idx in range(1, len(scores)):
		if scores[idx] > scores[idx-1]:
			rewards[idx] = rewards[idx-1] + 1
		# because when to 'right' we assign only once
		# but when to 'left' then we may reassign rewards existing
		# => no max() required

	for idx in reversed(range(len(scores) - 1)):
		if scores[idx] > scores[idx+1]:
			rewards[idx] = max(rewards[idx], rewards[idx+1]+1)

	return sum(rewards)

# 4 Four Number Sum
def fourNumberSum(array, targetSum):
    quadruplet = []
	ht = {}
	# add to ht sums of pairs
	# which are behind our current number
	for idx1 in range(1, len(array) - 1):
		# (above) we used '1' as we don't do anything
		# throughout first pass
		# (below) for numbers that come after current (idx1)
		for idx2 in range(idx1 + 1, len(array)):
			curr_sum = array[idx1] + array[idx2]
			diff = targetSum - curr_sum
			if diff in ht: # => found quadruplet
				for pair in ht[diff]:
					quadruplet.append(pair + [array[idx1], array[idx2]])
		# (below) for numbers that come before current (idx1)
		for idx3 in range(0, idx1):
			curr_sum = array[idx1] + array[idx3]
			if curr_sum not in ht:
				ht[curr_sum] = [[array[idx3], array[idx1]]]
			else:
				ht[curr_sum].append([array[idx3], array[idx1]])
		# those 2 loops above are for not
		# double counting quadruplets
	return quadruplet

