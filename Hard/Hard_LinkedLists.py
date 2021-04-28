# 1 Find Loop
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# T: O(n S: O(n)
def findLoop(head):
	ht = {}

	while True:
		if head not in ht:
			ht[head] = True
			head = head.next
		else:
			return head

# T: O(n) S: O(1)
def findLoop(head):
	first = head
	second = head

	while True:
		first = first.next
		second = second.next.next
		if first == second:
			break

	first = head
	while first != second:
		first = first.next
		second = second.next

	return first

# same as above just minor tweaks
def findLoop(head):
	first = head.next
	second = head.next.next

	while first != second:
		first = first.next
		second = second.next.next

	first = head
	while first != second:
		first = first.next
		second = second.next

	return first


# 2 Reverse Linked LIst
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	node = head
	nx = None
	pr = None

	while node:
		nx = node.next
		node.next = pr
		pr = node
		node = nx

	return pr

# 3 Merge Linked Lists
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
	p1 = headOne
	p2 = headTwo
	prev = None
	
	while p1 and p2:
		if p1.value < p2.value:
			prev = p1
			p1 = p1.next
		else:
			if prev is not None:
				prev.next = p2
			prev = p2
			p2 = p2.next
			prev.next = p1
	# if p1 moved further to None
	if p1 is None:
		prev.next = p2

	return headOne if headOne.value < headTwo.value else

# 4 Shift Linked List
# mine

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 4 variables required: old head/old tail/new head/new tail
# old tail -> old head; newHead -> newTail.next; newTail.next -> None
# newTail.next is newHead => getting newTail will grant us newHead 'for free'
# newTail is located 'k positions away' from old tail when k > 0
# whilst when k < 0 => abs(k) from old head
def shiftLinkedList(head, k):
	i = 0
	tail = head
	while tail.next:
		tail = tail.next
		i += 1
	i += 1 # to have the real length
	
	offset = abs(k) % i
	# a) if k == 0 b) if k % i == 0 (30 % 6)
	if offset == 0:
		return head
	# in Python modulo will return positive integer
	newTailPos = i - offset if k > 0 else offset
	newTail = head
	count = 1
	# Ex: newTailPos = 4 => we need exactly 4th position
	# hence starting from 0 will move us one ahead
	while count != newTailPos:
		newTail = newTail.next
		count += 1
	
	newHead = newTail.next
	tail.next = head
	newTail.next = None
	
	return newHead

# not mine
def shiftLinkedList(head, k):
    tail = head
	length = 1
	while tail.next:
		tail = tail.next
		length += 1
	
	offset = abs(k) % length
	if offset == 0:
		return head
	
	newTailPos = length - offset if k > 0 else offset
	newTail = head
	
	for i in range(1, newTailPos):
		newTail = newTail.next
	
	newHead = newTail.next
	newTail.next = None
	tail.next = head
	
	return newHead
