# 1 Remove duplicates from Linked List
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
	curr = linkedList
	while curr:
		next_curr = curr.next
		while next_curr and next_curr.value == curr.value:
			next_curr = next_curr.next
		curr.next = next_curr
		curr = next_curr
	return linkedList
