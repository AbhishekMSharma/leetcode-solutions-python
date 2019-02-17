class Node:
	def __init__ (self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__ (self):
		self.root = None
		
	def append(self, value):
		if (self.root == None):
			self.next = Node(value)
		else:
			self.next.append(value)
			
	def printLinkedList(self):
		if (self.next == None):
			return
		else:
			print(self.value)
			self.next.printLinkedList()
			
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.append(7)
linked_list.printLinkedList()