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
