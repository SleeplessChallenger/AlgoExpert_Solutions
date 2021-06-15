# 1 LRU Cache
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


# 2 Rearrange Linked List
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
	curr = head
	smallerHead = None
	smallerTail = None
	biggerHead = None
	biggerTail = None
	equalHead = None
	equalTail = None
	
	while curr:
		if curr.value < k:
			smallerHead, smallerTail = getAdjacent(curr, smallerHead, smallerTail)
		elif curr.value > k:
			biggerHead, biggerTail = getAdjacent(curr, biggerHead, biggerTail)
		else:
			equalHead, equalTail = getAdjacent(curr, equalHead, equalTail)
		# use `prevNode` to exclude possible bugs
		# when new node still points to another node
		# which it has previosly precede
		prevNode = curr
		curr = curr.next
		prevNode.next = None

	smaller_equalHead, smaller_equalTail = connectLists(smallerHead, smallerTail,
													    equalHead, equalTail)
	newHead, newTail = connectLists(smaller_equalHead, smaller_equalTail,
								    biggerHead, biggerTail)
	# `newHead` instead of `smaller_equalHead` as
	# we can have `k` < every value in LinkedList
	# => only bigHead & bigTail
	return newHead

def getAdjacent(node, head, tail):
	# newHead = head
	
	# we can get by wihtout newHead,
	# but newTail is essential.
	# a) if tail is None we are
	# to specify that our tail is
	# updated
	# b) but if tail is not None,
	# then we can't assign `node` to it
	# as it'll be rewritten, we're to add
	# new node via `.next` property
	newTail = node
	if head is None:
		head = node
	# not simply return `newTail`
	# but also chain previous tail
	# with new one
	if tail is not None:
		tail.next = node
	
	return head, newTail

def connectLists(smallHead, smallTail, bigHead, bigTail):	
	# we need smallHead if it exists as
	# we're to return eventual new head
	# -> only if it's None choose bigHead
	newHead = bigHead if smallHead is None else smallHead
	
	# we need bigTail if it exists as
	# we're to connect next part (bigger one)
	# to it -> only if bigTail is None choose smallTail
	newTail = smallTail if bigTail is None else bigTail
	
	if smallTail:
		smallTail.next = bigHead
	
	return newHead, newTail
