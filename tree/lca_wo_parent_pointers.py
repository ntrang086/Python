"""Find the lowest common ancestor in a binary tree without using parent pointers."""

from bst import BinarySearchTree
from nary_tree import NArayTree, Node

def find_ancestors(root, current_node, path):
    """Find a list of ancestors of current_node starting from root. 
    A node is an ancestor of itself"""
    if root is None or current_node is None:
        return path
    path.append(root)
    if root.key == current_node.key:
        return path
    # Find ancestors starting on the left branch and update path
    find_ancestors(root.left, current_node, path)
    if current_node in path:
        return path 
    # If current_node is not in the left branch, search the right one
    else:
        find_ancestors(root.right, current_node, path)
        if current_node in path:
            return path
    path.pop()
    return path

def lowest_common_ancestor(root, node_1, node_2):
    """Find the lowest common ancestor of two nodes starting from root."""
    ancestors_1 = find_ancestors(root, node_1, [])
    ancestors_2 = find_ancestors(root, node_2, [])
    if len(ancestors_1) == 0 or len(ancestors_2) == 0:
        return None
    i = 0
    while i < min(len(ancestors_1), len(ancestors_2)):
        if ancestors_1[i].key != ancestors_2[i].key:
            break
        i += 1
    return ancestors_1[i - 1]

if __name__ == "__main__":
    print ("Create a Binary Search Tree")
    bst = BinarySearchTree()
    test_list = [8, 3, 1, 6, 4, 7, 10, 14, 13, 14]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        bst.insert(element)
    bst.print_tree()
    print ("LCA for 3 and 10:", 
        lowest_common_ancestor(bst.root, bst.root.left, bst.root.right).key)
    node_1 = bst.root.left.left
    node_14 = bst.root.right.right
    print ("LCA for 1 and 14:", lowest_common_ancestor(bst.root, node_1, node_14).key)
    node_7 = bst.root.left.right.right
    print ("LCA for 1 and 7:", lowest_common_ancestor(bst.root, node_1, node_7).key)

    print ("Create a Binary Tree")
    binary_tree = NArayTree(is_binary=True)
    test_list = [15, 8, 5, 2]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        binary_tree.insert(element, binary_tree.root)
    binary_tree.print_tree()
    root = binary_tree.root
    node_2 = binary_tree.root.left.left
    node_5 = binary_tree.root.right
    print ("LCA for 2 and 5:", 
        lowest_common_ancestor(root, node_2, node_5).key)
    print ("LCA for 2 and 8:", 
        lowest_common_ancestor(root, node_2, root.left).key)
    print ("LCA for 8 and 2:", 
        lowest_common_ancestor(root, root.left, node_2).key)
    print ("LCA for 2 and 5 with 8 as root:", 
        lowest_common_ancestor(root.left, node_2, node_5))
    print ("LCA for 2 and None:", 
        lowest_common_ancestor(root, node_2, None))
