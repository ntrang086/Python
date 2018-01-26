"""Implement a Binary Search Tree with insert, delete, search and other functions"""

class Node:
    """A node in a Binary Search Tree. Each node has info about its key, parent 
    (if any), and children (if any)."""

    def __init__(self, key):
        """Create a node from a key."""
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def get_children(self):
        """Retrieve children (if any) of a node."""
        children = []
        if self.left is not None:
            children.append(self.left.key)
        if self.right is not None:
            children.append(self.right.key)
        return children


class BinarySearchTree():
    """A binary search tree: each node has a key and has two subtrees. The key 
    in each node must be greater than or equal to any key stored in the left 
    subtree, and less than or equal to any key stored in the right subtree."""

    def __init__(self, root=None):
        """Create a Binary Search Tree."""
        self.root = root

    def insert(self, key):
        """Insert a key into the tree."""
        if self.root is None:
            self.root = Node(key)
        else:
            self.__insert_node(key, self.root)
    
    def __insert_node(self, key, current_node, parent=None):
        """Private function to be used by insert(). Insert a key by comparing it
        with the key of current_node. Assign parent and children (if any) to the
        new node."""

        if key == current_node.key:
            print ("Key {} already exists".format(key))
            return
        elif key < current_node.key:
            if current_node.left:
                self.__insert_node(key, current_node.left, current_node)
            else:
                current_node.left = Node(key)
                current_node.left.parent = current_node
        else:
            if current_node.right:
                self.__insert_node(key, current_node.right, current_node)
            else:
                current_node.right = Node(key)
                current_node.right.parent = current_node
    
