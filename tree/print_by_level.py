"""Print a tree by level"""

from collections import deque
from nary_tree import NArayTree, Node

def print_nodes_by_level(root):
    """Print nodes by level."""
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        for i in range(len(queue)):
            node = queue.popleft()
            print (node.key, "", end="")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print ("")

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
    binary_tree.insert(6, node_5)
    print_nodes_by_level(binary_tree.root)