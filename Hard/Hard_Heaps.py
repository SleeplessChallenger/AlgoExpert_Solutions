# 1 Continuous Median

# 1. maxHeap where lower bound and minHeap where upper bound

# 2. if new number < max in maxHeap: append to lower
#    elif new number > max in maxHeap: append to upper

# 3. when adding to either lower or upper bound: siftUp

# if difference between heaps > 1 (actually 2): rebalance
# 	if len(lower bound) > len(upper bound): take [0] (biggest) and add to upper
# 	elif len(lower bound) < len(upper bound): take [0] (smallest) and add to lower

# 	then siftDown() either of the heaps

# 4. median will be the biggest from the bounds [0] number

# 5. comapre() comprises comparision of numbers

class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
		self.lower = Heap([], maxHeap)
		self.greater = Heap([], minHeap)

    def insert(self, number):
        if not self.lower.length or number < self.lower.peek():
			self.lower.insert(number)
		else:
			self.greater.insert(number)
		self.rebalance()
		self.updateMedian()
	
	def rebalance(self):
		if self.lower.length - self.greater.length == 2:
			self.greater.insert(self.lower.remove())
		elif self.greater.length - self.lower.length == 2:
			self.lower.insert(self.greater.remove())
	
	def updateMedian(self):
		if self.lower.length == self.greater.length:
			self.median = (self.lower.peek() + self.greater.peek()) / 2
		elif self.lower.length > self.greater.length:
			self.median = self.lower.peek()
		else:
			self.median = self.greater.peek()

    def getMedian(self):
        return self.median


class Heap:
	def __init__(self, arr, compare):
		self.heap = self.buildHeap(arr)
		self.length = len(self.heap)
		self.compare = compare
	
	def buildHeap(self, heap):
		parentIdx = (len(heap) - 1) // 2
		for idx in reversed(range(parentIdx + 1)):
			self.siftDown(idx, len(heap) - 1)
		return heap
	
	def siftDown(self, idx, length):
		childOne = idx * 2 + 1
		while childOne <= length:
			childTwo = idx * 2 + 2 if (idx * 2 + 2) <= length else -1
			#if self.heap[childTwo] != -1 and self.heap[childTwo] < self.heap[childOne]:
			if childTwo != -1:
				if self.compare(self.heap[childTwo], self.heap[childOne]):
					swap = childTwo
				else:
					swap = childOne
			else:
				swap = childOne
			#if self.heap[swap] < self.heap[idx]:
			if self.compare(self.heap[swap], self.heap[idx]):
				self.swap(idx, swap, self.heap)
				idx = swap
				childOne = idx * 2 + 1
			else:
				return
			
	def siftUp(self):
		idx = len(self.heap) - 1
		while idx > 0:
			parentIdx = (idx - 1) // 2
			if self.compare(self.heap[idx], self.heap[parentIdx]):
			# if self.heap[parentIdx]   self.heap[idx]:
				self.swap(parentIdx, idx, self.heap)
				idx = parentIdx
			else:
				return
	
	def peek(self):
		return self.heap[0]
	
	def remove(self):
		to_remove = self.heap[0]
		node = self.heap.pop()
		if len(self.heap) > 0:
			self.heap[0] = node
			self.length -= 1
			self.siftDown(0, self.length - 1)
		return to_remove
	
	def insert(self, value):
		self.heap.append(value)
		self.length += 1
		self.siftUp()
	
	def swap(self, a, b, arr):
		arr[a], arr[b] = arr[b], arr[a]


def minHeap(a, b):
	return a < b

def maxHeap(a, b):
	return a > b

# 2 Sort K-Sorted Array
def sortKSortedArray(array, k):
	heap = MinHeap(array[: min(k + 1, len(array))])
	
	sortedIdx = 0
	for idx in range(k + 1, len(array)):
		node = heap.remove()
		array[sortedIdx] = node
		sortedIdx += 1
		nextNode = array[idx]
		heap.insert(nextNode)
	
	while not heap.check():
		node = heap.remove()
		array[sortedIdx] = node
		sortedIdx += 1
	
	return array


class MinHeap:
	def __init__(self, arr):
		self.heap = self.buildHeap(arr)
	
	def check(self):
		return len(self.heap) == 0
	
	def buildHeap(self, arr):
		parentIdx = (len(arr) - 2) // 2
		for i in reversed(range(parentIdx + 1)):
			self.siftDown(i, len(arr) - 1, arr)
		return arr
	
	def peek(self):
		return self.heap[0]
	
	def remove(self):
		to_remove = self.heap[0]
		node = self.heap.pop()
		if len(self.heap) > 0:
			self.heap[0] = node
			self.siftDown(0, len(self.heap) - 1, self.heap)
		return to_remove
	
	def insert(self, value):
		self.heap.append(value)
		self.siftUp()
	
	def siftDown(self, idx, length, arr):
		idxOne = idx * 2 + 1
		while idxOne <= length:
			idxTwo = idx * 2 + 2 if idx * 2 + 2 <= length else -1
			if idxTwo != -1 and arr[idxOne] > arr[idxTwo]:
				swap = idxTwo
			else:
				swap = idxOne
			
			if arr[swap] < arr[idx]:
				self.swapValues(swap, idx, arr)
				idx = swap
				idxOne = idx * 2 + 1
			else:
				return
	
	def swapValues(self, i, j, arr):
		arr[i], arr[j] = arr[j], arr[i]
	
	def siftUp(self):
		idx = len(self.heap) - 1
		while idx > 0:
			parentIdx = (idx - 1) // 2
			if self.heap[idx] < self.heap[parentIdx]:
				self.swapValues(idx, parentIdx, self.heap)
				idx = parentIdx
			else:
				return
