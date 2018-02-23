"""Find the distance between 2 nodes in a normal binary tree.
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
    # Keep going left until finding the node or until returning -1
    left_distance = distance_from_lca(lca.left, current_node, distance + 1)
    if left_distance != -1:
        return left_distance
    # If node was not found on left branch, search on the right one
    else:
        return distance_from_lca(lca.right, current_node, distance + 1)

def distance_between_nodes(root, node_1, node_2):
    lca = lowest_common_ancestor(root, node_1, node_2)
    node_1_from_lca = distance_from_lca(lca, node_1, 0)
    node_2_from_lca = distance_from_lca(lca, node_2, 0)
    return node_1_from_lca + node_2_from_lca

if __name__ == "__main__":
    print ("Create a Binary Tree")
    binary_tree = NArayTree(is_binary=True)
    test_list = [15, 8, 5, 2, 3]
    print ("Insert the elements from the following list:", test_list)
    for element in test_list:
        print ("Insert", element)
        binary_tree.insert(element, binary_tree.root)
    binary_tree.print_tree()
    root = binary_tree.root
    node_8 = binary_tree.root.left
    node_2 = binary_tree.root.left.left
    node_3 = binary_tree.root.left.right
    node_5 = binary_tree.root.right
    print ("distance from root to 8:", 
        distance_from_lca(root, node_8, 0))
    print ("distance from root to 2:", 
        distance_from_lca(root, node_2, 0))
    print ("distance from root to 3:", 
        distance_from_lca(root, node_3, 0))
    print ("distance from root to 5:", 
        distance_from_lca(root, node_5, 0))

    print ("distance between 8 and 2:", 
        distance_between_nodes(root, node_8, node_2))
    print ("distance between 8 and 5:", 
        distance_between_nodes(root, node_8, node_5))
    print ("distance between 2 and 5:", 
        distance_between_nodes(root, node_5, node_2))
    print ("distance between 3 and 5:", 
        distance_between_nodes(root, node_5, node_3))
    