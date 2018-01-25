"""Implement a BST with insert and delete functions"""

class Node:

	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

	def get_children():
		children = []
		if self.left is not None:
			children.append(self.left)
		if self.right is not None:
			children.append(self.right)
		return children


class BinarySearchTree():
	def __init__(self, root=None):
		self.root = root

	def insert(self, root, key):
		if self.root is None:
			self.root = Node(key)
		elif key <= self.root.key:
			self.insert(self.root.left, key)
		else:
			self.insert(self.root.right, key)
		return root
