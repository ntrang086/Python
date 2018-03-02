"""Reverse a linked list iteratively and recursively.
Another way of doing so."""

from linked_list import *

def reverse_iteratively(linked_list):
    """Reverse a linked list iteratively."""
    previous_node = None
    current_node = linked_list.head
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    linked_list.head = previous_node
    return linked_list

def reverse_recursively_util(linked_list, previous_node, current_node):
    """Helper function for reverse_recursively."""
    # Base case: if we reach the end of the linked list
    if current_node.next is None:
        current_node.next = previous_node
        linked_list.head = current_node
        return linked_list
    next_node = current_node.next
    current_node.next = previous_node
    return reverse_recursively_util(linked_list, current_node, next_node)

def reverse_recursively(linked_list):
    """Reverse a linked list recursively."""
    if linked_list.head is None:
        return linked_list
    return reverse_recursively_util(linked_list, None, linked_list.head)


if __name__ == "__main__":
    # Initialize a LinkedList with a head that has key 1
    linked_list = LinkedList(Node(1))
    linked_list.append(2)
    linked_list.append(3)
    linked_list = reverse_iteratively(linked_list)

    # Should print 3, 2, and 1 respectively
    print (linked_list.get_position(1).key)
    print (linked_list.get_position(2).key)
    print (linked_list.get_position(3).key)

    linked_list = reverse_recursively(linked_list)
    # Should print 1, 2, and 3 respectively
    print (linked_list.get_position(1).key)
    print (linked_list.get_position(2).key)
    print (linked_list.get_position(3).key)