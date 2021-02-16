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
