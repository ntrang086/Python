"""Reverse a linked list iteratively and recursively."""

from linked_list import *

def reverse_iteratively(linked_list):
    """Reverse a linked list iteratively."""
    reverse_linked_list = LinkedList()
    current_node = linked_list.head
    while current_node:
        reverse_linked_list.insert(current_node.key, 1)
        current_node = current_node.next
    return reverse_linked_list

def reverse_recursively(linked_list, reverse_linked_list):
    """Reverse a linked list recursively."""
    current_node = linked_list.head
    if current_node is None:
        return reverse_linked_list
    reverse_linked_list.insert(current_node.key, 1)
    linked_list.delete_head()
    return reverse_recursively(linked_list, reverse_linked_list)


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

    linked_list = reverse_recursively(linked_list, LinkedList())
    # Should print 1, 2, and 3 respectively
    print (linked_list.get_position(1).key)
    print (linked_list.get_position(2).key)
    print (linked_list.get_position(3).key)