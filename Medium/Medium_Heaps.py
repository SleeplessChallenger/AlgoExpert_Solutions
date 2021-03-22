# 1 Min Heap Construction
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, arr):
    	parent_idx = (len(arr) - 2) // 2
    	# -2 here because we need to take into account 2 values
    	for x in reversed(range(parent_idx + 1)):
    		self.siftDown(idx=x, heap=arr, length=len(arr)-1)
    	return arr
    	# we go from middle to start

    def siftDown(self, idx=None, heap=None, length=None):
    	if idx is None:
    		idx = 0
    		length = len(self.heap)
    		element = self.heap[0]
    		while True:
    			leftIdx = idx * 2 + 1
    			rightIdx = idx * 2 + 2
    			swap = None
    			if leftIdx < length:
    				leftChild = self.heap[leftIdx]
    				if leftChild < element:
    					swap = leftIdx
    			if rightIdx < length:
    				rightChild = self.heap[rightIdx]
    				if (swap == None and rightChild < element) or (swap != None and rightChild < leftChild):
    					swap = rightChild
    			if swap is None:
    				break
    			self.heap[idx] = self.heap[swap]
    			self.heap[swap] = element
    			idx = swap
    		return
    	else:
    		childOneidx = idx * 2 + 1
    		while childOneidx <= length:
    			childTwoidx = idx * 2 + 2 if idx * 2 + 2 <= length else -1
    			if childTwoidx != -1 and heap[childTwoidx] < heap[childOneidx]:
    				swap = childTwoidx
    			else:
    				swap = childOneidx
    			if heap[swap] < heap[idx]:
    				heap[swap], heap[idx] = heap[idx], heap[swap]
    				idx = swap
    				childOneidx = 2 * idx + 1
    			else:
    				return

    def siftUp(self):
    	idx = len(self.heap) - 1
    	while idx > 0:
    		parentIdx = (idx - 1) // 2
    		if self.heap[parentIdx] > self.heap[idx]:
    			self.heap[parentIdx], self.heap[idx] = self.heap[idx], self.heap[parentIdx]
    			idx = parentIdx
    		else:
    			break

    def peek(self):
    	return self.heap[0]

    def insert(self, value):
    	self.heap.append(value)
    	self.siftUp()

    def remove(self):
    	remove_value = self.heap[0]
    	node = self.heap.pop()
    	if len(self.heap) > 0:
    		self.heap[0] = node
    		self.siftUp()
    	return remove_value
