"""Find the distance between 2 nodes in a BST.
Dist(n1, n2) = Dist(lca, n1) + Dist(lca, n2)
"""

from bst import BinarySearchTree
from nary_tree import NArayTree, Node
from lca_wo_parent_pointers import lowest_common_ancestor


def distance_from_lca(lca, current_node, distance):
    """Calculate the distance from lca to current_node."""
    if lca is None or current_node is None:
        return -1
    if lca.key == current_node.key:
        return distance
    # If lca.key > current_node.key, search the left branch
    if lca.key > current_node.key:
        return distance_from_lca(lca.left, current_node, distance + 1)
    # Otherwise, search the right one
    else:
        return distance_from_lca(lca.right, current_node, distance + 1)

def distance_between_nodes(root, node_1, node_2):
    lca = lowest_common_ancestor(root, node_1, node_2)
    node_1_from_lca = distance_from_lca(lca, node_1, 0)
    node_2_from_lca = distance_from_lca(lca, node_2, 0)
    return node_1_from_lca + node_2_from_lca

if __name__ == "__main__":
    print ("Create a Binary Search Tree")
    bst = BinarySearchTree()
    test_list = [8, 3, 1, 6, 4, 7, 10, 14, 13, 14]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        bst.insert(element)
    bst.print_tree()
    root = bst.root
    node_3 = root.left
    node_10 =root.right
    node_1 = root.left.left
    node_14 = root.right.right
    node_7 = node_3.right.right
    
    print ("distance from root to 3:", 
        distance_from_lca(root, node_3, 0))
    print ("distance from root to 10:", 
        distance_from_lca(root, node_10, 0))
    print ("distance from root to 1:", 
        distance_from_lca(root, node_1, 0))
    print ("distance from root to 14:", 
        distance_from_lca(root, node_14, 0))
    print ("distance from root to 7:", 
        distance_from_lca(root, node_7, 0))

    print ("distance between 3 and 10:", 
        distance_between_nodes(root, node_3, node_10))
    print ("distance between 3 and 1:", 
        distance_between_nodes(root, node_3, node_1))
    print ("distance between 7 and 14:", 
        distance_between_nodes(root, node_7, node_14))
    