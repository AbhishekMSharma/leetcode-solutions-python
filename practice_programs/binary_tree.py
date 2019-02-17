class TreeNode:
	def __init__ (self, value):
		self.value = value
		self.left = None
		self.right = None

	def insertToTree(self, value):
		if self.value:
			if value < self.value:
				if self.left is None:
					self.left = TreeNode(value)
				else:
					self.left.insertToTree(value)
			elif value > self.value:
				if self.right is None:
					self.right = TreeNode(value)
				else:
					self.right.insertToTree(value)
			else:
				self.value = value
	
	def inOrderTraversal(self):
		if self.left:
			self.left.inOrderTraversal()
		print (self.value)
		if self.right:
			self.right.inOrderTraversal()
				
binary_tree = TreeNode(5)
binary_tree.insertToTree(7)
binary_tree.insertToTree(4)
binary_tree.insertToTree(8)
binary_tree.inOrderTraversal()