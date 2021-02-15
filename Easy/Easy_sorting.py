# 1 Bubble sort
def bubbleSort(arr):
	i = len(arr) - 1
	j = 0
	while i > 0:
		noSwaps = True
		while j < i:
			if arr[j + 1] < arr[j]:
				arr[j + 1], arr[j] = arr[j], arr[j + 1]
				noSwaps = False
				j += 1
			else:
				j += 1
		if noSwaps:
			return arr
		i -= 1
		j = 0
	return arr

# 2 Selection sort
def selectionSort(arr):
	i = 0
	j = i + 1
	while i < len(arr):
		min_ = i
		while j < len(arr):
			if arr[j] < arr[min_]:
				min_ = j
				j += 1
			else:
				j += 1
		if min_ != i:
			arr[min_], arr[i] = arr[i], arr[min_]
		i += 1
		j = i + 1
	return arr

# 3 Insertion sort
def insertionSort(arr):
	i = 1
	j = i -1
	while i < len(arr):
		min_ = arr[i]
		while j >= 0 and arr[j] > min_:
			arr[j + 1] = arr[j]
			j += 1
		arr[j + 1] = min_
		i += 1
		j = i - 1
	return arr
