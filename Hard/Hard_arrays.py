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
			left = left - 1
			current += 1

		while right in ht:
			right = right + 1
			current += 1

		if longest < current:
			longest = current
			result = [left + 1, right - 1]

	return result
