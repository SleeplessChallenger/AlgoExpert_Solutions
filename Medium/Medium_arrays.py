# 1 Three number sum
#mine
def threeSum(arr, target):
	left = 0
	right = len(arr) - 1
	arr.sort()
	result = []
	temp = 0
	while temp < len(arr):
		while left < right:
			sum_ = arr[temp] + arr[left] + arr[right]
			if sum_ > target:
				right -= 1
			elif sum_ < target:
				left += 1
			else:
				result.append([arr[temp], arr[left], arr[right]])
				left += 1
				right -= 1
		temp += 1
		left = temp + 1
		right = len(arr) - 1
	return result

#not mine
def threeNumberSum(arr, target):
	arr.sort()
	result = []
	for x in range(len(arr) - 2):
		left = x + 1
		right = len(arr) - 1
		while left < right:
			total = arr[x] + arr[left] + arr[right]
			if total > target:
				right -= 1
			elif total < target:
				left += 1
			else:
				result.append([arr[x], arr[left], arr[right]])
				left += 1
				right -= 1
	return result

# 2 Smallest difference
# mine
def helper(obj, arr):
	temp2 = None
	for y in arr:
		if temp2 is None or abs(temp2[0] - temp2[1]) > abs(obj - y):
			temp2 = [obj, y]
	return temp2

def smallest(arr1, arr2):
	temp = None
	result = None
	for x in arr1:
		temp = helper(x, arr2)
		if result is None or abs(result[0] - result[1]) > abs(temp[0] - temp[1]):
			result = [temp[0], temp[1]]
	return result

# not mine
def smallestDif(arr1, arr2):
	arr1.sort()
	arr2.sort()
	idx1 = 0
	idx2 = 0
	smallest = float('inf')
	current = float('inf')
	cont = []
	while idx1 < len(arr1) and idx2 < len(arr2):
		first = arr1[idx1]
		second = arr2[idx2]
		if first > second:
			current = first - second
			idx2 += 1
		elif first < second:
			current = second - first
			idx1 += 1
		else:
			return [first, second]
		if smallest > current:
			smallest = current
			cont = [first, second]
	return cont

# 3 Move element to End
# mine
def moveElementToEnd(arr, toMove):
	left = 0
	right = len(arr) - 1
	while left <= right:
		if arr[left] == toMove and arr[right] == toMove:
			right -= 1
		elif arr[left] == toMove and arr[right] != toMove:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
		elif arr[left] != toMove and arr[right] != toMove:
			left += 1
		else:
			left += 1
			right -= 1
	return arr

# not mine
def moveElementToEnd(arr, toMove):
	i = 0
	j = len(arr) - 1
	while i < j:
		while i < j and arr[j] == toMove:
			j -= 1
		if arr[i] == toMove:
			arr[i], arr[j] = arr[j], arr[i]
		i += 1
	return arr

# 4 Monotonic array
# mine
def isMonotonic(arr):
	if len(arr) == 0 or len(arr) == 1:
		return True
	for x in range(1, len(arr)):
		if arr[x] > arr[x-1]:
			for y in range(2, len(arr)):
				if arr[y] >= arr[y-1]:
					continue
				else:
					return False
			break
		elif arr[x] < arr[x-1]:
			for y in range(2, len(arr)):
				if arr[y] <= arr[y-1]:
					continue
				else:
					return False
			break
	return True
 # not mine a
def isMonotonic(arr):
	nonIncr = True
	nonDecr = True
	for x in range(1, len(arr)):
		if arr[x] > arr[x-1]:
			nonDecr = False
		if arr[x] < arr[x-1]:
			nonIncr = False
	return nonIncr or nonDecr

# not mine b
def isMonotonic(arr):
	if len(arr) <= 2:
		return True
	direction = arr[1] - arr[0]
	for x in range(2, len(arr)):
		if direction == 0:
			direction = arr[x] - arr[x-1]
			continue
		if func(direction, arr[x-1], arr[x]):
			return False
	return True

def func(direction, prev, curr):
	difference = curr - prev
	if direction > 0:
		return difference < 0
	return difference > 0

# 5 Spiral Traverse
# iterative
def spiralTraverse(arr):
	result = []
	st_r, end_r = 0, len(arr) - 1
	st_c, end_c = 0, len(arr[0]) - 1
	while st_r <= end_r and st_c <= end_c:
		for a in range(st_c, end_c + 1):
			result.append(arr[st_r][a])
		for b in range(st_r + 1, end_r + 1):
			result.append(arr[b][end_c])
		for c in reversed(range(st_c, end_c)):
			# end_c in range is exclusive 
			# what we need not to double count
			if st_r == end_r:
				break
			result.append(arr[end_r][c])
		for d in reversed(range(st_r + 1, end_r)):
			if st_r == end_r:
				break
			result.append(arr[d][st_c])
		st_c += 1
		end_c -= 1
		st_r += 1
		end_r -= 1
	return result

# recursive
def spiralTraverse(arr):
	result = 0
	helper(arr, result, 0, len(arr) - 1, 0, len(arr[0]) - 1)
	return result

def helper(arr, result, st_r, end_r, st_c, end_c):
	if st_r > end_r or st_c > end_c:
		return
	for a in range(st_c, end_c + 1):
		result.append(arr[st_r][a])
	for b in range(st_r + 1, end_r + 1):
		result.append(arr[b][end_c])
	for c in reversed(range(st_c, end_c)):
		if st_r == end_r:
			break
		result.append(arr[end_r][c])
	for d in reversed(range(st_r + 1, end_r)):
		if st_c == end_c:
			break
		result.append(arr[d][st_c])
	helper(arr, result, st_r + 1, end_r - 1, st_c + 1, end_c - 1)

# 6 Longest Peak
# mine
def longestPeak(arr):
	if len(arr) < 3:
		return 0
	current_left, current_right = 0, 0
	longest = 0
	for x in range(1, len(arr)):
		left = x - 1
		right = x + 1
		while left >= 0:
			if arr[left] < arr[left + 1] and arr[left] < arr[x]:
				current_left += 1
			else:
				break
			left -= 1
		while right < len(arr) - 1:
			if arr[right] < arr[right - 1] and arr[right] < arr[x]:
				current_right += 1
			else:
				break
			right += 1
		if current_right == 0 or current_left == 0:
			current_left, current_right = 0, 0
			continue
		longest = max(longest, current_left + current_right)
		current_left, current_right = 0, 0
	return 1 + longest if longest != 0 else 0

# not mine
def longestPeak(arr):
	longest = 0
	i = 1
	while i < len(arr) - 1:
		tip = arr[i] > arr[i - 1] and arr[i] > arr[i + 1]
		if not tip:
			i += 1
			continue
		left = i - 2
		while left >= 0 and arr[left] < arr[left + 1]:
			left -= 1
		right = i + 2
		while right < len(arr) and arr[right] < arr[right - 1]:
			right += 1
		curr = right - left - 1
		longest = max(longest, curr)
		i = right
	return longest

# 7 Array of Products
# mine
def arrayOfProducts(arr):
	new_arr = []
	temp = 1
	for x in range(len(arr)):
		for y in reversed(range(len(arr))):
			if x != y:
				temp *= arr[y]
		new_arr.append(temp)
		temp = 1
	return new_arr

# not mine (a)
def arrayOfProducts(arr):
	new_arr = [1 for x in range(len(arr))]
	new_arr1 = [1 for x in range(len(arr))]
	new_arr2 = [1 for x in range(len(arr))]

	curr = 1
	# we put multiplied product to the left
	# the left of arr[0] is 1
	for x in range(len(arr)):
		new_arr1[x] = curr
		curr *= arr[x]

	curr = 1
	for x in reversed(range(len(arr))):
		new_arr2[x] = curr
		curr *= arr[x]

	for x in range(len(arr)):
		new_arr[x] = new_arr1[x] * new_arr2[x]

	return new_arr

# not mine (b)
def arrayOfProducts(arr):
	new_arr = [1 for x in range(len(arr))]

	curr = 1
	for x in range(len(arr)):
		new_arr[x] = curr
		curr *= arr[x]

	curr = 1
	for x in reversed(range(len(arr))):
		new_arr[x] *= curr
		curr *= arr[x]

	return new_arr

# 8 First Duplicate Value
# mine
def firstDuplicateValue(arr):
	ht = {}
	for x in arr:
		if x not in ht:
			ht[x] = 0
		ht[x] += 1
		if ht[x] > 1:
			return x
	return -1

# not mine
# in descr it's said that integers in array
# are between 1 and n inclusive, where 
# n is the length of the array
# => we can use trick with indicies
def firstDuplicateValue(arr):
	for x in arr:
		absV = abs(x)
		if arr[absV - 1] < 0:
			return absV
		arr[absV - 1] *= -1
	return -1

# 9 Merge Overlapping Intervals
def mergeOverlappingIntervals(intervals):
	if len(intervals) <= 1:
		return intervals

	intervals.sort(key=lambda x: x[0])

	current = intervals[0]
	result = [current]

	for next_int in intervals:

		if next_int[0] <= current[1]:
			current[1] = max(next_int[1], current[1])

		else:
			result.append(next_int)
			current = next_int

	return result
