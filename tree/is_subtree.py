"""Check if a binary tree is subtree of another binary tree."""

from bst import BinarySearchTree
from collections import deque

def search(key, current_node):
    """Search for a key in a binary tree starting with current_node 
    using Breadth First Search."""
    if current_node is None or key == current_node.key:
        return current_node
    queue = deque()
    queue.append(current_node)
    while len(queue) > 0:
        node = queue.popleft()
        if node.key == key:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None

def is_the_same_tree(node_1, node_2):
    """Check if the tree starting with node_1
    is the same as the tree starting with node_2"""
    if node_1 is None and node_2 is None:
        return True
    if node_1 is None or node_2 is None:
        return False
    return node_1.key == node_2.key \
            and is_the_same_tree(node_1.left, node_2.left) \
            and is_the_same_tree(node_1.right, node_2.right)

def is_subtree(small_tree_root, big_tree_root):
    """Check if the tree starting with small_tree_root is
    a subtree of big_tree_root, assuming that we have"""
    if small_tree_root is None and big_tree_root is None:
        return True
    if small_tree_root is None or big_tree_root is None:
        return False
    # Check if the small_tree_root exists in the big tree
    subtree_root = search(small_tree_root.key, big_tree_root)
    # Check if the tree starting with small_tree_root is the
    # same as the subtree starting with subtree_root
    return is_the_same_tree(small_tree_root, subtree_root)

if __name__ == "__main__":
    print ("Create a Binary Search Tree that is not a sum tree")
    bst = BinarySearchTree()
    test_list = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        bst.insert(element)
    bst.print_tree()
    node_3 = bst.root.left
    
    print ("Create a Binary Search Tree that is a subtree of the previous one")
    bst2 = BinarySearchTree()
    test_list2 = [3, 1, 6, 4, 7]
    for element in test_list2:
        bst2.insert(element)
    bst2.print_tree()
    print (is_the_same_tree(node_3, bst2.root))
    print (is_subtree(bst2.root, bst.root))
    print (is_subtree(bst.root, None))
    print (is_subtree(None, None))
