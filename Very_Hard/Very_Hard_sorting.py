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
