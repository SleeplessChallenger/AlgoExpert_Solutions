class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
		self.bucket = LinkedList()
		self.cache = {}
		self.size = 0

    def insertKeyValuePair(self, key, value):
		if key not in self.cache:
			if self.currSize() < self.maxSize:
				self.size += 1
			else:
				self.evict_lru()
			# `key` is also essential as
			# without it we cannot get
			# least recent in O(1)
			self.cache[key] = Node(key, value)
		else:
			self.replace_value(key, value)
		# mru - most recently used
		self.replace_mru(self.cache[key])

    def getValueFromKey(self, key):
        if key not in self.cache:
			return None
		self.replace_mru(self.cache[key])
		return self.cache[key].value

    def getMostRecentKey(self):
		if self.bucket.head is None:
			return None
		return self.bucket.head.key
        
	def currSize(self):
		return len(self.cache)
	
	def evict_lru(self):
		# remove .tail
		linked_list = self.bucket.tail
		linked_list_key = linked_list.key
		self.bucket.remove_tail()
		self.cache.pop(linked_list_key)
	
	def replace_value(self, k, v):
		self.cache[k].value = v
	
	def replace_mru(self, node):
		# node = (key, value)
		self.bucket.update_head(node)


class LinkedList:
	def __init__(self):
		# .head & .tail will be k-v pair
		self.head = None
		self.tail = None

	def update_head(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
			
		elif self.head == self.tail:
			self.tail.prev = node
			self.head = node
			self.head.next = self.tail
		
		else:
			if self.tail == node:
				# when we place node to
				# be the .head, but it
				# occupies .tail
				self.remove_tail()
			# (below) work with adjacent nodes		
			node.remove_adjacent()
			# (below) work with .head
			self.head.prev = node
			node.next = self.head
			self.head = node
			
	def remove_tail(self):
		if self.tail is None:
			return
		elif self.head == self.tail:
			self.head = None
			self.tail = None
			return
		else:
			self.tail = self.tail.prev
			self.tail.next = None


class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None
	
	def remove_adjacent(self):
		if self.prev is not None:
			self.prev.next = self.next
			
		if self.next is not None:
			self.next.prev = self.prev
		
		self.next = None
		self.prev = None
