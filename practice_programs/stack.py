class StackNode:
	def __init__ (self, data):
		self.data = data
		self.next = None
		
class myStack:
	def __init__ (self):
		self.top = None
		
	def push(self, data):
		if self.top == None:
			self.top = StackNode(data)
		else:
			temp = self.top
			self.top = StackNode(data)
			self.top.next = temp
			
	def pop(self):
		if self.top == None:
			print ("Empy stack")
		else:
			self.top = self.top.next
	
	def peek(self):
		if self.top == None:
			print ("Empty stack")
		else:
			print (self.top.data)

		
s = myStack()
s.push(5)
s.push(1)
s.push(3)
s.pop()
s.pop()
s.push(8)
s.peek()
s.pop()
s.peek()