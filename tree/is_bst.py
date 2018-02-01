"""Check if a tree is a bst"""

from collections import deque
from bst import BinarySearchTree

def is_binary_search_tree(current_node):
    """Check if a tree starting with current_node is a binary tree"""
    is_bst = True
    queue = deque()
    if current_node:
        queue.append(current_node)
    while len(queue) > 0:
        node = queue.popleft()
        num_children = len(node.get_children())
        if num_children > 2:
            is_bst = False
        # The subsequent conditions apply to binary trees only
        elif num_children == 2:
            is_bst = (node.right.key > node.key > node.left.key and
                      is_max_node(node) and is_min_node(node))
            queue.append(node.left)
            queue.append(node.right)
        elif node.left:
            is_bst = is_max_node(node)
            queue.append(node.left)
        elif node.right:
            is_bst = is_min_node(node)
            queue.append(node.right)
        if is_bst == False:
            return is_bst
    return is_bst

def get_subtree(current_node):
    """Get the subtree starting from current_node."""
    subtree = []
    subtree += [current_node]
    if current_node.left:
        subtree += get_subtree(current_node.left)
    if current_node.right:
        subtree += get_subtree(current_node.right)
    return subtree


def is_min_node(current_node):
    """Check if current_node is has the min key compared with its right descendants"""
    right_subtree = get_subtree(current_node.right)
    for node in right_subtree:
        if current_node.key > node.key:
            return False
    return True

def is_max_node(current_node):
    """Check if current_node is has the max key compared with its left descendants"""
    left_subtree = get_subtree(current_node.left)
    for node in left_subtree:
        if current_node.key < node.key:
            return False
    return True


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


if __name__ == "__main__":
    print ("Create a Binary Search Tree")
    bst = BinarySearchTree()
    test_list = [8, 3, 1, 6, 4, 7, 10, 14, 13, 14]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        bst.insert(element)

    tree = bst.get_tree(bst.root)
    print ("\nPrint the tree in Depth First order")
    bst.print_tree()
    assert is_binary_search_tree(bst.root)

    print ("Create a Binary Tree which is not a Binary Search Tree")
    is_binary = True
    non_bst = NArayTree(is_binary=is_binary)
    non_bst_list = [8, 3, 10]
    print ("Insert the elements from the following list:", non_bst_list)
    for element in non_bst_list:
        assert is_binary_search_tree(non_bst.root)
        non_bst.insert(element, non_bst.root)

    print ("\nInsert 6 as a right child for node 3")
    node_3 = non_bst.root.left
    node_6 = non_bst.insert(6, node_3, left=False)
    assert is_binary_search_tree(non_bst.root)

    print ("\nInsert 2 as a left child for node 6")
    node_2 = non_bst.insert(2, node_6, left=True)
    assert is_binary_search_tree(non_bst.root) == False
    assert is_binary_search_tree(node_3) == False

    print ("\nRemove 2")
    node_6.left = None
    node_6.children = []
    assert is_binary_search_tree(non_bst.root)

    print ("\nInsert 9 as a right child for node 6")
    node_9 = non_bst.insert(9, node_6, left=False)
    assert is_binary_search_tree(non_bst.root) == False

    print ("\nRemove 9")
    node_6.right = None
    node_6.children = []
    assert is_binary_search_tree(non_bst.root)

    print ("\nInsert 14 as a right child for node 10")
    node_14 = non_bst.insert(14, non_bst.root.right, left=False)
    assert is_binary_search_tree(non_bst.root)

    print ("\nInsert 7 as a left child for node 14")
    node_7 = non_bst.insert(7, node_14)
    assert is_binary_search_tree(non_bst.root) == False
    assert is_binary_search_tree(node_14)

    print ("\nPrint the tree in Depth First order")
    non_bst.print_tree()

    