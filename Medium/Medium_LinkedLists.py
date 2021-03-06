# 1 Linked List Construction
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
    	if not self.head:
    		self.head = node
    		self.tail = self.head
    		return
    	self.insertBefore(self.head, node)

    def setTail(self, node):
    	if not self.tail:
    		self.setHead(node)
    		return
    	self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
    	if self.head == nodeToInsert and self.tail == nodeToInsert:
    		return
    	self.remove(nodeToInsert)
    	if node.prev is None:
    		self.head = nodeToInsert
    	else:
    		node.prev.next = nodeToInsert
    	node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
    	if self.head == nodeToInsert and self.tail == nodeToInsert:
    		return
    	self.remove(nodeToInsert)
    	if node.next is None:
    		self.tail = nodeToInsert
    	else:
    		node.next.prev = nodeToInsert
    	node.next = nodeToInsert

    def insertAtPosition(self, position, node):
    	if position == 1:
    		self.setHead(node)
    		return
    	count = 1
    	curr = self.head
    	while curr and count != position:
    		count += 1
    		curr = curr.next
    	if not curr:
    		self.setTail(node)
    	else:
    		self.insertBefore(node)

    def removeNodesWithValue(self, value):
    	curr = self.head
    	while curr:
    		prev = curr
    		curr = curr.next
    		if prev.value == value:
    			self.remove(prev)

    def remove(self, node):
    	if self.head == node:
    		self.head = self.head.next
    	if self.tail == node:
    		self.tail = self.tail.prev
    	self.remove_two(node)

    def remove_two(self, node):
    	if node.next:
    		node.next.prev = node.prev
    	if node.prev:
    		node.prev.next = node.next
    	node.next = None
    	node.prev = None

    def contains(self, value):
    	if self.head == value and self.tail == value:
    		return True
    	curr = self.head
    	while curr:
    		if curr.value == value:
    			return True
    		else:
    			curr = curr.next
    	return False

    	# another way
    	if self.head == value and self.tail == value:
    		return True
    	curr = self.head
    	while curr and curr.value != value:
    		curr = curr.next
    	if not curr:
    		return False
    	return True


# 2 Remove Kth node from end
# mine
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    length = 0
    curr = head
    while curr:
        curr = curr.next
        length += 1
    if (length - k) == 0:
        head.value = head.next.value
        head.next = head.next.next
        return
    count = 0
    while count != (length - k) + 1:
        count += 1
        if (length - k) == count:
            head.next = head.next.next
            break
        head = head.next

# not mine
def removeKthNodeFromEnd(head, k):
    first = head
    second = head
    counter = 1
    # with '1' and '<=' we can make one step further
    # and if k = 4 land at fifth position so as in the
    # final loop easily use .next.next property.
    # inated of 1 it's possible: counter = 0 and while counter < k
    while counter <= k:
        counter += 1
        second = second.next
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second is not None:
        second = second.next
        first = first.next
    first.next = first.next.next

# 3 Sum of Linked Lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(link1, link2):
    # there are 3 scopes: link1, link2
    # and our new LinkedList
    newHead = LinkedList(0)
    curr = newHead 
    # we need to return .head
    curr1 = link1
    curr2 = link2
    carry = 0

    while curr1 or curr2 or carry != 0:
        # take values of link1 and link2 nodes
        nodeVal1 = curr1.value if curr1 else 0
        nodeVal2 = curr2.value if curr2 else 0
        total = nodeVal1 + nodeVal2 + carry

        # take value without carry
        newValue = total % 10
        newNode = LinkedList(newValue)

        # in our new LinkedList we place .next to 
        # current node and make current node that .next one
        curr.next = newNode
        curr = newNode

        # receive the very carry
        carry = total // 10
        curr1 = curr1.next if curr1 else None
        curr2 = curr2.next if curr2 else None

    return newHead.next

