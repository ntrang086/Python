"""Check if a tree is a bst"""

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

