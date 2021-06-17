# 1 Merge Sorted Arrays
# mine
def mergeSortedArrays(arr):
	result = []
	temp = [0 for _ in arr]
	while True:
		idx = None
		smallest = float('inf')
		for i in range(len(arr)):
			if temp[i] >= len(arr[i]):
				continue
			num = arr[i][temp[i]]
			if smallest > num:
				smallest = num
				idx = i
				
		if smallest == float('inf'):
			break
		result.append(smallest)
		temp[idx] += 1

	return result		

# first
# T: O(n*k) S: O(n + k)
def mergeSortedArrays(arr):
# mine
    idxArr = [0 for _ in arr]
	result = []

	while True:
		temp = []
		for x in range(len(arr)):
			idx = idxArr[x]
			# condition if idx exceeds length
			if idx == len(arr[x]):
				temp.append(float('inf'))
			else:
				temp.append(arr[x][idx])
			
		# break condition
		if min(temp) == float('inf'):
			break
		value = min(temp)
		result.append(value)
		# move idx in idxArr
		i = temp.index(value)
		idxArr[i] += 1
	
	return result

# not mine
	result = []
	idxArr = [0 for _ in arr]
	while True:
		temp = []
		for x in range(len(arr)):
			currArr = arr[x]
			currIdx = idxArr[x]
			if currIdx == len(currArr):
				continue
			temp.append({'num': currArr[currIdx], 'idx': x})

		if len(temp) == 0:
			break
		minValue = getItem(temp)
		result.append(minValue['num'])
		idxArr[minValue['idx']] += 1
	return result
	
def getItem(arr):
	minIdx = 0
	for i in range(1, len(arr)):
		if arr[i]['num'] < arr[minIdx]['num']:
			minIdx = i
	return arr[minIdx] 

# second
# T: O(n*log(k) + k) S: O(n + k)
def mergeSortedArrays(arr):
	result = []
	idxArr = []
	# populate with first values from
	# all subarrays of arr
	for x in range(len(arr)):
		idxArr.append({'idx': x, 'eleIdx': 0, 'num': arr[x][0]})
	heap = MinHeap(idxArr)

	while heap.check() is not True:
		smallest = heap.remove()
		idx, eleIdx, num = smallest['idx'], smallest['eleIdx'], smallest['num']
		result.append(num)
		# check to prevent IndexError
		if eleIdx == len(arr[idx]) - 1:
			continue
		# `idx` will never change as it denotes position
		# of subarray within an array
		# `eleIdx` will change if we take it
		# `num` will be from `arr` where `eleIdx` will
		# give us the next value
		heap.insert({'idx': idx, 'eleIdx': eleIdx + 1, 'num': arr[idx][eleIdx + 1]})
	
	return result
	
	
class MinHeap:
	def __init__(self, arr):
		self.heap = self.buildHeap(arr)
	
	def buildHeap(self, arr):
		parentIdx = (len(arr) - 1) // 2
		for i in reversed(range(parentIdx + 1)):
			self.siftDown(i, len(arr) - 1, arr)
		return arr
	
	def check(self):
		return len(self.heap) == 0
	
	def siftDown(self, idx, length, heap):
		idxOne = idx * 2 + 1
		while idxOne <= length:
			idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
			if idxTwo != -1 and heap[idxTwo]['num'] < heap[idxOne]['num']:
				swap = idxTwo
			else:
				swap = idxOne
			if heap[swap]['num'] < heap[idx]['num']:
				self.swapFunc(swap, idx, heap)
				idx = swap
				idxOne = idx * 2 + 1
			else:
				return
	
	def remove(self):
		drop = self.heap[0]
		value = self.heap.pop()
		if len(self.heap) > 0:
			self.heap[0] = value
			self.siftDown(0, len(self.heap) - 1, self.heap)
		return drop
	
	def peek(self):
		return self.heap[0]
	
	def insert(self, value):
		self.heap.append(value)
		self.siftUp()
	
	def siftUp(self):
		idx = len(self.heap) - 1
		while idx > 0:
			parentIdx = (idx - 1) // 2
			if self.heap[parentIdx]['num'] > self.heap[idx]['num']:
				self.swapFunc(idx, parentIdx, self.heap)
				idx = parentIdx
			else:
				return
	
	def swapFunc(self, i, j, arr):
		arr[i], arr[j] = arr[j], arr[i]
