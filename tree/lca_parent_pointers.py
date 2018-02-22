"""Find the lowest common ancestor in a BST and binary tree using parent pointers."""

from bst import BinarySearchTree
from nary_tree import NArayTree, Node

def lowest_common_ancestor(node_1, node_2):
    """Find the lowest common ancestor of two nodes"""
    ancestors = set()
    while node_1:
        ancestors.add(node_1)
        node_1 = node_1.parent
    while node_2:
        if node_2 in ancestors:
            return node_2
        node_2 = node_2.parent
    return None

if __name__ == "__main__":
    print ("Create a Binary Search Tree that is not a sum tree")
    bst = BinarySearchTree()
    test_list = [8, 3, 1, 6, 4, 7, 10, 14, 13, 14]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        bst.insert(element)
    bst.print_tree()
    print ("LCA for 3 and 10:", 
        lowest_common_ancestor(bst.root.left, bst.root.right).key)
    node_1 = bst.root.left.left
    node_14 = bst.root.right.right
    print ("LCA for 1 and 14:", lowest_common_ancestor(node_1, node_14).key)
    node_7 = bst.root.left.right.right
    print ("LCA for 1 and 7:", lowest_common_ancestor(node_1, node_7).key)

    print ("Create a Binary Tree")
    binary_tree = NArayTree(is_binary=True)
    test_list = [15, 8, 5, 2]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        binary_tree.insert(element, binary_tree.root)
    binary_tree.print_tree()
    print ("LCA for 2 and 5:", 
        lowest_common_ancestor(binary_tree.root.left.left, binary_tree.root.right).key)
