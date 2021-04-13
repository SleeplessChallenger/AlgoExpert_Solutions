# 1 QuickSort
# mine
def quickSort(arr):
	small = []
	medium = []
	big = []

	if len(arr) > 1:
		pivot = arr[0]

		for x in arr:
			if pivot > x:
				small.append(x)
			elif pivot < x:
				big.append(x)
			else:
				medium.append(x)
		return quickSort(small) + medium + quickSort(big)
	else:
		return arr

# not mine
def quickSort(array):
	sort(array, 0, len(array) - 1)
	return array

def sort(arr, start, end):
	if start >= end:
		return

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
	leftSubArrIsSmall = right - 1 - start < end - (right + 1)
	# leftSubArr starts at right idx - 1 and
	# rightSubArr starts at right idx + 1
	if leftSubArrIsSmall:
		sort(arr, start, right - 1)
		sort(arr, right + 1, end)
	else:
		sort(arr, right + 1, end)
		sort(arr, start, right - 1)

def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]


# 2 Heap Sort
def heapSort(array):
	buildHeap(array)
	for idx in reversed(range(1, len(array))):
		swap_func(0, idx, array)
		siftDown(0, idx - 1, array)
	return array

def buildHeap(heap):
	parentIdx = (len(heap) - 2) // 2 # -1 also OK
	for idx in reversed(range(parentIdx + 1)):
		siftDown(idx, len(heap) - 1, heap)

def siftDown(idx, length, heap):
	idxOne = idx * 2 + 1
	while idxOne <= length:
		idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
		if idxTwo != -1 and heap[idxTwo] > heap[idxOne]:
			swap = idxTwo
		else:
			swap = idxOne
		if heap[swap] > heap[idx]:
			swap_func(swap, idx, heap)
			idx = swap
			idxOne = idx * 2 + 1
		else:
			return 

def swap_func(i, j, heap):
	heap[i], heap[j] = heap[j], heap[i]
