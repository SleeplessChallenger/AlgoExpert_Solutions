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
