"""Check if a linked list has a loop.
Find the node at the beginning of the loop."""

from linked_list import *

def has_loop(linked_list):
    """Check if a linked list has a loop"""
    seen_nodes = set()
    current_node = linked_list.head
    while current_node:
        if current_node in seen_nodes:
            return True
        seen_nodes.add(current_node)
        current_node = current_node.next
    return False

if __name__ == "__main__":
    # Initialize a LinkedList with a head that has key 1
    linked_list = LinkedList(Node(1))
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    node_5 = linked_list.get_position(5)
    node_5.next = linked_list.get_position(2)
    print (has_loop(linked_list))