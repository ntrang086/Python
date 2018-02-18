"""Check if a tree is a bst"""

from collections import deque
from bst import BinarySearchTree
from nary_tree import NArayTree

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

    