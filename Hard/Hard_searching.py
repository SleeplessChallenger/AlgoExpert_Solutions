# 1 Shifted Binary Search
def shiftedBinarySearch(array, target):
	# T: O(n) S: O(1)
	if target in array:
		return array.index(target)
	return -1

	# T: O(log n) S: O(1)
	left = 0
	right = len(array) - 1

	while left <= right:
		middle = (left + right) // 2

		if array[middle] == target:
			return middle

		elif array[middle] >= array[left]:
			if target >= array[left] and target < array[middle]:
				right = middle - 1
			else:
				left = middle + 1

		elif array[middle] < array[right]:
		# else
			if array[middle] < target and target <= array[right]:
				left = middle + 1
			else:
				right = middle - 1

	return -1

# 2 Search for Range
# 1 T: O(n) S: O(1)
def searchForRange(array, target):
	idx = None
	for value in range(len(array)):
		if array[value] == target:
			idx = value
			break

	if idx is None:
		return [-1, -1]

	count = idx
	for i in range(idx + 1, len(array)):
		if array[i] == target:
			count += 1
		else:
			break

	return [idx, count]

# 2 T: O(log n) S: O(1)
def searchForRange(array, target):
	idxRange = [-1, -1]
	helper(array, target, 0, len(array) - 1, idxRange, True)
	helper(array, target, 0, len(array) - 1, idxRange, False)
	return idxRange

def helper(array, target, left, right, idxRange, goLeft):
	while left <= right:
		middle = (left + right) // 2
		if array[middle] < target:
			left = middle + 1
		elif array[middle] > target:
			right = middle - 1
		else:
			if goLeft:
				# check if middle == 0
				if middle == 0 or array[middle - 1] != target:
					idxRange[0] = middle
					return
				else:
					right = middle - 1
			else:
				if middle == len(array) - 1 or array[middle + 1] != target:
					idxRange[1] = middle
					return
				else:
					left = middle + 1
