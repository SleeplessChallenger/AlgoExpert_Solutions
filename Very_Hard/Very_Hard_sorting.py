# 1 Merge Sort
# mine
# T: O(n * log n) S: O(n * log n)
def merge(a,b):
	lst = list()
	i = 0
	j = 0
	while i < len(a) and j < len(b):
		if b[j] > a[i]:
			lst.append(a[i])
			i += 1
		else:
			lst.append(b[j])
			j += 1

	while i < len(a):
		lst.append(a[i])
		i += 1

	while j < len(b):
		lst.append(b[j])
		j += 1

	return lst

def mergeSort(arr):
	if len(arr) == 1:
		return arr
	arr1 = mergeSort(arr[:len(arr)//2])
	arr2 = mergeSort(arr[len(arr)//2:])
	return merge(arr1, arr2)

# not mine
# T: O(n * log n) S: O(n)
def mergeSort(arr):
	if len(arr) <= 1:
		return arr
	aux = arr[:]
	mergeHelper(arr, 0, len(arr) - 1, aux)
	return arr

def mergeHelper(arr, left, right, aux):
	if left == right:
		return arr
	middleIdx = (left + right) // 2
	mergeHelper(aux, left, middleIdx, arr)
	mergeHelper(aux, middleIdx + 1, right, arr)
	doMerge(arr, aux, left, right, middleIdx)

def doMerge(arr, aux, left, right, middleIdx):
	start = left
	auxStart = left
	fromMiddle = middleIdx + 1
	
	while auxStart <= middleIdx and fromMiddle <= right:
		if aux[fromMiddle] >= aux[auxStart]:
			arr[start] = aux[auxStart]
			auxStart += 1
		else:
			arr[start] = aux[fromMiddle]
			fromMiddle += 1
		start += 1
	
	while auxStart <= middleIdx:
		arr[start] = aux[auxStart]
		auxStart += 1
		start += 1
	
	while fromMiddle <= right:
		arr[start] = aux[fromMiddle]
		fromMiddle += 1
		start += 1

# 2 Count Inversions
# T: O(n*log n) S: O(n)

# inversion in left + inversion in right
# + inversion in both => total num of inversions

# `len(array) - idx = inversions` in left array as
# we insert num from right array before ALL the 
# nums in left array (if curr in left > curr in right).
# Because left array initially should be before right,
# we don't care if something in `right > left`
def countInversions(arr):
    return count_merge(arr, 0, len(arr))

def count_merge(arr, start, end):
	# <= not == as can be: []
	if end - start <= 1:
		return 0
	
	middle = (start + end) // 2
	leftInv = count_merge(arr, start, middle)
	rightInv = count_merge(arr, middle, end)
	# called after prev. two as we want
	# out array to be sorted
	bothInv = mergePart(arr, start, middle, end)
	return leftInv + rightInv + bothInv

def mergePart(arr, start, middle, end):
	sortedArr = []
	left = start
	right = middle
	inv = 0

	while left < middle and right < end:
		if arr[left] > arr[right]:
			inv += middle - left
			sortedArr.append(arr[right])
			right += 1
		else:
			sortedArr.append(arr[left])
			left += 1

	while left < middle:
		sortedArr.append(arr[left])
		left += 1
		
	while right < end:
		sortedArr.append(arr[right])
		right += 1
	
	# sortedArr += arr[left:middle] + arr[right:end]
	
	for i in range(len(sortedArr)):
		arr[start + i] = sortedArr[i]
	
	return inv
