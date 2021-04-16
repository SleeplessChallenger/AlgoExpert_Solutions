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

