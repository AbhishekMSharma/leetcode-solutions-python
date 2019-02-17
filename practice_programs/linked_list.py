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
			
	# delete node at position 8 -> 10 -> 3 -> 4 -> 7
	def deleteNodeAtPosition(self, position):
		if position == 0:
			#current = self.head.next
			self.head = self.head.next
			return
		
		current_position = 0
		current = self.head
		while (current):
			if current_position+1 == position:
				#t = current.next
				current.next = current.next.next
				return
			current = current.next
			current_position += 1
			
	def getLength(self):
		if self.head is None: return 0
		current = self.head
		length = 0
		while(current):
			length += 1
			current = current.next
		return length
		
	def getIndexOfNode(self, data):
		if self.head is None: return -1
		current = self.head
		current_position = 0
		while (current):
			if current.data == data:
				return current_position
			current_position += 1
			current = current.next
		return -1
		
	def getNodeAtPosition(self, position):
		if position == 0: return self.head.data
		current = self.head.next
		current_position = 1
		while (current):
			if current_position == position:
				return current.data
			current_position += 1
			current = current.next
			
	# 8 -> 10 -> 3 -> 5 -> 7 -> 2
	def getNthNodeFromEnd(self, position):
		linked_list_length = self.getLength()
		position = linked_list_length - position
		print ("Position", position)
		return self.getNodeAtPosition(position)
		
	def getMiddleOfLinkedList(self):
		slow_pointer = fast_pointer = self.head
		while fast_pointer and fast_pointer.next:
			fast_pointer = fast_pointer.next.next
			slow_pointer = slow_pointer.next
		return slow_pointer.data
		
	def isLinkedListPalindrome(self):
		current = self.head
		data_values = list()
		while(current):
			data_values.append(current.data)
			current = current.next
		
		return True if data_values == data_values[::-1] else False
		
	# 2 -> 2 -> 3 -> 4 -> 4 -> 5 -> 8 -> 8 -> 9
	def removeDuplicatesSorted(self):
		current = self.head
		previous_data = ''
		while(current):
			if current.data != previous_data:
				original_node = current
				previous_data = current.data
				current = current.next
			else:
				original_node.next = current.next
				current = current.next
		return self.head
				
	# 8 -> 3 -> 2 -> 4
	# next -> 3, 8 -> None, prev -> 8, current -> 3
	# next -> 2, 3 -> 8, prev -> 3, current -> 2
	# next -> 4, 2 -> 3, prev -> 2, current -> 4
	# next -> None, 4 -> 2, prev -> 4, current -> None
	# head -> 4 -> 2 -> 3 -> 8 -> None
	def reverseLinkedList(self):
		current = self.head
		prev = next = None
		while (current):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev
		
	
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
linked_list.deleteNodeAtPosition(3)
linked_list.printLinkedList()
print("Linked List Length:",linked_list.getLength())
print("Linked List get index of data 8: ", linked_list.getIndexOfNode(10))
print("Linked List get element at index 2: ", linked_list.getNodeAtPosition(2))
print("Linked List get element at 3rd position from end: ", linked_list.getNthNodeFromEnd(3))
print("Middle element of Linked List: ", linked_list.getMiddleOfLinkedList())
print("Is Linked List Palindrome: ", linked_list.isLinkedListPalindrome())
linked_list_2 = LinkedList()
linked_list_2.append(3)
linked_list_2.append(3)
linked_list_2.append(3)
linked_list_2.append(4)
linked_list_2.append(4)
linked_list_2.append(6)
linked_list_2.append(7)
linked_list_2.append(7)
linked_list_2.append(8)
linked_list_2.printLinkedList()
linked_list_2.removeDuplicatesSorted()
linked_list_2.printLinkedList()
linked_list_2.reverseLinkedList()
linked_list_2.printLinkedList()