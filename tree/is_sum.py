"""Check if a tree is a sum tree"""

from bst import BinarySearchTree
from nary_tree import NArayTree

def get_subtree(current_node):
    subtree = [current_node]
    if current_node.left:
        subtree += get_subtree(current_node.left)
    if current_node.right:
        subtree += get_subtree(current_node.right)
    return subtree

def sum_children(current_node):
    if current_node is None:
        return 0
    if current_node.left is None and current_node.right is None:
        return current_node.key
    children = get_subtree(current_node)[1:]
    sum_children = 0
    for node in children:
        sum_children += node.key
    return sum_children

def is_sum_tree(current_node):
    return sum_children(current_node) == current_node.key

if __name__ == "__main__":
    print ("Create a Binary Search Tree that is not a sum tree")
    bst = BinarySearchTree()
    test_list = [8, 3, 1, 6, 4, 7, 10, 14, 13, 14]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        bst.insert(element)

    tree = bst.get_tree(bst.root)
    print ("\nPrint the tree in Depth First order")
    bst.print_tree()
    assert is_sum_tree(bst.root) == False

    print ("Create a Binary Tree that is a sum tree")
    sum_tree = NArayTree(is_binary=True)
    test_list = [15, 8, 5, 2]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        sum_tree.insert(element, sum_tree.root)

    tree = sum_tree.get_tree(sum_tree.root)
    print ("\nPrint the tree in Depth First order")
    sum_tree.print_tree()
    assert is_sum_tree(sum_tree.root)

    print ("\nInsert 2 and 6 as children of node 8")
    node_8 = sum_tree.root.left
    node_2 = sum_tree.insert(2, node_8)
    node_6 = sum_tree.insert(6, node_8)
    assert is_sum_tree(sum_tree.root) == False

    print ("\nInsert 1 and 5 as children for node 6")
    node_1 = sum_tree.insert(1, node_6)
    assert is_sum_tree(sum_tree.root) == False
    node_5 = sum_tree.insert(5, node_6)
    assert is_sum_tree(node_6)

