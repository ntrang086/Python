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

