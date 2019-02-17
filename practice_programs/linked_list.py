class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__ (self):
		self.head = None
	
	# add new node at the end
	def append(self, data):
		if (self.head == None):
			self.head = Node(data)
		else:
			last = self.head
			while (last.next):
				last = last.next
			last.next = Node(data)
			
	# add new node at the start
	def prepend(self, data):
		if (self.head == None):
			self.head = Node(data)
		else:
			temp = self.head
			self.head = Node(data)
			self.head.next = temp
			
	# insert after values
	def insertAfterValue(self, value, data):
		current = self.head
		while(current):
			if current.data == value:
				new_node = Node(data)
				new_node.next = current.next
				current.next = new_node
				return
			current = current.next
		
		# if value not found, appending data at the end
		self.append(data)
		
	# delete a node
	def deleteNode(self, data):
		current = self.head
		while (current):
			t = current.next
			if t.data == data:
				current.next = t.next
				return
			current = current.next
	
	def printLinkedList(self):
		print ("Printing Linked List")
		current = self.head
		while (current):
			print(current.data)
			current = current.next
			
	
			
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.prepend(8)
linked_list.insertAfterValue(8,10)
linked_list.append(7)
linked_list.insertAfterValue(7,11)
linked_list.printLinkedList()
linked_list.deleteNode(11)
linked_list.append(8)
linked_list.printLinkedList()