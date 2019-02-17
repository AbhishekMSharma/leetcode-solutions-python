class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__ (self):
		self.head = None
		
	def append(self, data):
		if (self.head == None):
			self.head = Node(data)
		else:
			last = self.head
			while (last.next):
				last = last.next
			last.next = Node(data)
	
	def printLinkedList(self):
		current = self.head
		while (current):
			print(current.data)
			current = current.next
			
	
			
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.append(7)
linked_list.printLinkedList()