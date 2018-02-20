"""Check if a tree is a sum tree"""

from bst import BinarySearchTree
from nary_tree import NArayTree, Node

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
    if current_node is None:
        return True
    return (sum_children(current_node) == current_node.key) \
            and is_sum_tree(current_node.left) \
            and is_sum_tree(current_node.right)

if __name__ == "__main__":
    print ("Create a Binary Search Tree that is not a sum tree")
    bst = BinarySearchTree()
    test_list = [8, 3, 1, 6, 4, 7, 10, 14, 13, 14]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        bst.insert(element)

    print ("\nPrint the tree in Depth First order")
    bst.print_tree()
    assert is_sum_tree(bst.root) == False

    assert is_sum_tree(None)

    print ("Create a Binary Tree")
    binary_tree = NArayTree(is_binary=True)
    test_list = [15, 4, 7]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        binary_tree.insert(element, binary_tree.root)
    assert is_sum_tree(binary_tree.root) == False

    print ("\nInsert another 4 as a child of node 4")
    node_4 = binary_tree.root.left
    node_4_new = Node(4, is_binary=True)
    node_4.left = node_4_new
    node_4.children.append(node_4_new)
    node_4_new.parent = node_4
    binary_tree.print_tree()
    assert is_sum_tree(binary_tree.root)
    assert is_sum_tree(node_4)
    assert is_sum_tree(node_4_new)

    print ("\nInsert 1 and 6 as children of node 7")
    node_7 = binary_tree.root.right
    node_1 = binary_tree.insert(1, node_7)
    node_6 = binary_tree.insert(6, node_7)
    binary_tree.print_tree()
    assert is_sum_tree(binary_tree.root) == False
    assert is_sum_tree(node_7)
    assert is_sum_tree(node_6)


    print ("Create another Binary Tree")
    binary_tree = NArayTree(is_binary=True)
    test_list = [15, 8, 5, 2]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        binary_tree.insert(element, binary_tree.root)
    assert is_sum_tree(binary_tree.root) == False
