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

    def delete():
        """Delete a key from the tree."""
        return
    
    def get_tree(self, current_node):
        """Get the tree with all its nodes."""
        tree = []
        if current_node is None:
            return tree
        tree += [current_node]
        if current_node.left:
            tree += self.get_tree(current_node.left)
        if current_node.right:
            tree += self.get_tree(current_node.right)
        return tree

    def print_tree(self):
        """Print out the key for each node in the tree."""
        print ([node.key for node in self.get_tree(self.root)])

    def get_child_parent(self, tree):
        """Output a list of tuples; each tuple contains a child and its parent."""
        child_parent_pairs = []
        for node in tree:
            if node.parent is not None:
                child_parent_pairs.append((node.key, node.parent.key))
            else:
                child_parent_pairs.append((node.key, node.parent))
        return child_parent_pairs

    def get_parent_children(self, tree):
        """Output a list of tuples; each tuple contain a node, its left child 
        and its right child."""
        parent_children = []
        for node in tree:
            if node.left is None:
                if node.right is None:
                    parent_children.append((node.key, node.left, node.right))
                else:
                    parent_children.append((node.key, node.left, node.right.key))
            else:
                if node.right is None:
                    parent_children.append((node.key, node.left.key, node.right))
                else:
                    parent_children.append((node.key, node.left.key, node.right.key))
        return parent_children


if __name__ == "__main__":
    print ("Create a Binary Search Tree")
    bst = BinarySearchTree()

    test_list = [8, 3, 1, 6, 4, 7, 10, 14, 13, 14]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        bst.insert(element)

    tree = bst.get_tree(bst.root)
    print ("\nPrint the tree")
    bst.print_tree()

    print ("\nThe root node is", bst.root.key)

    print ("\nGet pairs of children and their parent:", bst.get_child_parent(tree))
    print ("\nGet pairs of parents and their children:", bst.get_parent_children(tree))