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

# 3 Quickselect
# mine
def quickselect(array, k):
	k = k - 1
	return sort(array, 0, len(array) - 1, k)

def sort(arr, start, end, idx):
	pivot = start
	left = start + 1
	right = end


	while left <= right:
		if arr[pivot] < arr[left] and arr[pivot] > arr[right]:
			swap(arr, left, right)
		if arr[pivot] >= arr[left]:
			left += 1
		if arr[pivot] <= arr[right]:
			right -= 1
	swap(arr, right, pivot)
	# if our Pivot number
	# (right) > kth largest => disregard right part
	if right > idx:
		# end = right - 1
		return sort(arr, 0, right - 1, idx)
	# elif Pivot number < kth => disrgard left part
	elif right < idx:
		# start = right + 1
		return sort(arr, right + 1, end, idx)
	else:
		return arr[idx]
# we need to 'return' on all functions, because without it
# result of the arr[idx] will get lost in the
# call stack as those two functions don't return
# anything by themselves

def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

# not mine
def quickselect(array, k):
	k = k - 1
	return sort(array, 0, len(array) - 1, k)

def sort(arr, start, end, idx):
	while True:
		
		pivot = start
		left = start + 1
		right = end


		while left <= right:
			if arr[pivot] < arr[left] and arr[pivot] > arr[right]:
				swap(arr, left, right)
			if arr[pivot] >= arr[left]:
				left += 1
			if arr[pivot] <= arr[right]:
				right -= 1
		swap(arr, right, pivot)
		# if our Pivot number
		# (right) > kth largest => disregard right part
		if right > idx:
			end = right - 1
			# sort(arr, 0, right - 1, idx)
		# elif Pivot number < kth => disrgard left part
		elif right < idx:
			start = right + 1
			# sort(arr, right + 1, end, idx)
		else:
			return arr[idx]


def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]

# 4 Index Equals Values
# T: O(n) S: O(1)
def indexEqualsValue(array):
    # brute-force
	for x in range(len(array)):
		value = array[x]
		if value == x:
			return x
	return -1

# T: O(log n) S: O(1)
def indexEqualsValue(arr):
	left = 0
	right = len(arr) - 1
	# no duplicates in array & array is sorted!
	while left <= right:
		middle = (left + right) // 2
		target = arr[middle]
		
		if middle == 0 and middle == target:
			return middle
		
		elif middle == target and arr[middle - 1]  < middle - 1:
			return middle
		# if middle != 0 and if middle == target,
		# then check element to the left. if that
		# element < index -> return element from above
		# Why make only that check? Because idx cannot be
		# greater than value as array is sorted and have no
		# duplicates (and take into account that current value
		# == current idx and make one step to the left)
		# if arr[middle - 1] == middle - 1, then eliminate
		# right half of the algorithm. That's why we have
		# `else` statement
		# * because above we return if previous
		# index > previous value, but what if they're equal?
		# We don't return it here, but we need to do it further, that's
		# why use else to incorporate above mentioned case and when
		# value > idx
	
		elif middle > target:
			# all to the left can't match
			# as we're in sorted array
			left = middle + 1
		
		# we'll place `else` instead of `elif`. See
		# above big explanation for the reason
		else:
			# all to the right can't match
			# as we're in sorted array
			right = middle - 1
			
	return -1
