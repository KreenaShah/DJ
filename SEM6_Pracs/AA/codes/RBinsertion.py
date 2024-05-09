# Python code for the above approach
class RedBlackTree:
	class Node:
		def __init__(self, data):
			self.data = data
			self.left = None
			self.right = None
			self.colour = 'R'
			self.parent = None

	def __init__(self):
		self.root = None
		self.ll = False # Left-Left Rotation flag
		self.rr = False # Right-Right Rotation flag
		self.lr = False # Left-Right Rotation flag
		self.rl = False # Right-Left Rotation flag

	def rotateLeft(self, node):
		# Perform Left Rotation
		x = node.right
		y = x.left
		x.left = node
		node.right = y
		node.parent = x
		if y is not None:
			y.parent = node
		return x

	def rotateRight(self, node):
		# Perform Right Rotation
		x = node.left
		y = x.right
		x.right = node
		node.left = y
		node.parent = x
		if y is not None:
			y.parent = node
		return x

	def insertHelp(self, root, data):
		f = False # Flag to check RED-RED conflict

		if root is None:
			return self.Node(data)
		elif data < root.data:
			root.left = self.insertHelp(root.left, data)
			root.left.parent = root
			if root != self.root:
				if root.colour == 'R' and root.left.colour == 'R':
					f = True
		else:
			root.right = self.insertHelp(root.right, data)
			root.right.parent = root
			if root != self.root:
				if root.colour == 'R' and root.right.colour == 'R':
					f = True

		# Perform rotations
		if self.ll:
			root = self.rotateLeft(root)
			root.colour = 'B'
			root.left.colour = 'R'
			self.ll = False
		elif self.rr:
			root = self.rotateRight(root)
			root.colour = 'B'
			root.right.colour = 'R'
			self.rr = False
		elif self.rl:
			root.right = self.rotateRight(root.right)
			root.right.parent = root
			root = self.rotateLeft(root)
			root.colour = 'B'
			root.left.colour = 'R'
			self.rl = False
		elif self.lr:
			root.left = self.rotateLeft(root.left)
			root.left.parent = root
			root = self.rotateRight(root)
			root.colour = 'B'
			root.right.colour = 'R'
			self.lr = False

		# Handle RED-RED conflicts
		if f:
			if root.parent.right == root:
				if root.parent.left is None or root.parent.left.colour == 'B':
					if root.left is not None and root.left.colour == 'R':
						self.rl = True
					elif root.right is not None and root.right.colour == 'R':
						self.ll = True
				else:
					root.parent.left.colour = 'B'
					root.colour = 'B'
					if root.parent != self.root:
						root.parent.colour = 'R'
			else:
				if root.parent.right is None or root.parent.right.colour == 'B':
					if root.left is not None and root.left.colour == 'R':
						self.rr = True
					elif root.right is not None and root.right.colour == 'R':
						self.lr = True
				else:
					root.parent.right.colour = 'B'
					root.colour = 'B'
					if root.parent != self.root:
						root.parent.colour = 'R'
			f = False
		return root

	def inorderTraversalHelper(self, node):
		if node is not None:
			self.inorderTraversalHelper(node.left)
			print(node.data, end=" ")
			self.inorderTraversalHelper(node.right)

	def insert(self, data):
		if self.root is None:
			self.root = self.Node(data)
			self.root.colour = 'B'
		else:
			self.root = self.insertHelp(self.root, data)

	def inorderTraversal(self):
		self.inorderTraversalHelper(self.root)

t = RedBlackTree()
arr = [10,18,7,15,16,30,25,40,60,2,1,70]
for i in range(len(arr)):
	t.insert(arr[i])
	print()
	t.inorderTraversal()