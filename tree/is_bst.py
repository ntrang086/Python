"""Check if a tree is a bst"""

from collections import deque

class Node:
    """A node in a Tree. Each node has info about its key, parent 
    (if any), and children (if any). If is_binary is True, there will
    be information about its left and/or right children"""

    def __init__(self, key, is_binary=False):
        """Create a node from a key."""
        self.key = key
        self.parent = None
        self.children = []
        if is_binary:
            self.left = None
            self.right = None

    def get_children(self):
        """Retrieve children (if any) of a node."""
        return self.children

class NArayTree():
    """A non-binary tree with a root. Each node has an arbitrary number of children"""
    def __init__(self, root=None, is_binary=False):
        """Create a non-binary tree."""
        self.root = root
        self.is_binary = is_binary
    
    def insert(self, key, current_node, left=True):
        """Insert a key as a child of current_node. Prioritize inserting into the left
        tree is left is True."""
        new_node = Node(key, self.is_binary)
        new_node.parent = current_node
        if self.root is None:
            self.root = Node(key, self.is_binary)
        elif self.search(key, current_node):
            print ("Key {} already exists".format(key))
        elif self.is_binary == False:
            current_node.children.append(new_node)
        elif self.is_binary:
            if len(current_node.children) <= 1:
                current_node.children.append(new_node)
                if left:
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node.right = new_node
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node.left = new_node
            else:
                if left:
                    self.insert(key, current_node.left, left)
                else:
                    self.insert(key, current_node.right, left)
        return new_node

    def search(self, key, current_node):
        """Search for a key in the tree using Breadth First Search."""
        queue = deque()
        queue.append(current_node)
        while len(queue) > 0:
            node = queue.popleft()
            if node.key == key:
                return node
            if len(node.children) > 0:
                queue.extend(node.children)
        return None

    def get_tree(self, current_node):
        """Get the tree with all its nodes in Depth First order."""
        tree = []
        tree += [current_node]
        if current_node.left:
            tree += self.get_tree(current_node.left)
        if current_node.right:
            tree += self.get_tree(current_node.right)
        return tree

    def print_tree(self):
        """Print out the key for each node in the tree in Depth First order."""
        print ([node.key for node in self.get_tree(self.root)])

