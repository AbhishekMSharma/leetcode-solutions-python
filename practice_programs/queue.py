class QueueNode:
	def __init__ (self, data):
		self.data = data
		self.next = None
		
class myQueue:
	def __init__ (self):
		self.tail = None
	
	def addToQueue(self, data):
		if self.tail == None:
			self.tail = QueueNode(data)
		else:
			last = self.tail
			while last.next:
				last = last.next
			last.next = QueueNode(data)
			
	def removeFromQueue(self):
		if self.tail == None:
			print ("Empty queue")
		else:
			self.tail = self.tail.next
	
	def traverseQueue(self):
		print ("Traversing queue")
		if self.tail == None:
			print ("Empty queue")
		else:
			current = self.tail
			while current:
				print(current.data)
				current = current.next
				
q = myQueue()
q.addToQueue(3)
q.addToQueue(4)
q.addToQueue(8)
q.traverseQueue()
q.removeFromQueue()
q.traverseQueue()
			