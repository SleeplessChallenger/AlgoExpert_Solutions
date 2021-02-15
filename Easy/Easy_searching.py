# 1 Binary search
def binarySearch(arr, target):
	left = 0
	right = len(arr) - 1
	middle = (left + right) // 2
	while left <= right and arr[middle] != target:
		if arr[middle] > target:
			right = middle - 1
		else:
			left = middle + 1
		middle = (left + right) // 2
	if arr[middle] == target:
		return middle
	return -1

# 2 Three largest numbers
#mine
def findthreeLarges(arr):
	first, second, third = float('-inf'), float('-inf'), float('-inf')
	for x in arr:
		if x >= first:
			first, second, third = x, first, second
		elif x >= second:
			second, third = x, second
		elif x > third:
			third = x
	return [third, second, first]

#not mine
def findThreeLargestNumbers(arr):
	temp = [None, None, None]
	for x in arr:
		helper1(temp, x)
	return temp

def helper1(arr, y):
	if arr[2] is None or y > arr[2]:
		helper2(arr, y, 2)
	elif arr[1] is None or y > arr[1]:
		helper2(arr, y, 1)
	elif arr[0] is None or y > arr[0]:
		helper2(arr, y, 0)

def helper2(arr, a, num):
	for idx in range(num + 1):
		if idx < num:
			arr[idx] = arr[idx + 1]
		else:
			arr[idx] = a
