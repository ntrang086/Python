"""Clone a linked list that has a next pointer and the other pointer
points randomly at another node in the list"""

from doubly_linked_list import *

def clone_linked_list(linked_list):
    """Clone a randomly linked list. 
    Consider previous pointer the random pointer"""
    clone = DoublyLinkedList()
    # Create a dictionary with current_node as key and 
    # a new node with the same key as current_node
    seen = dict()
    if linked_list.head is None:
        return clone
    # Keep track of the current_node of the original linked list
    current_node = linked_list.head
    while current_node:
        if current_node not in seen:
            seen[current_node] = Node(current_node.key)
        # Update the current node of the clone linked list
        current_clone_node = seen[current_node]
        if current_node is linked_list.head:
            clone.head = current_clone_node
        if current_node.next:
            if current_node.next not in seen:
                seen[current_node.next] = Node(current_node.next.key)
            current_clone_node.next = seen[current_node.next]
        if current_node.previous:
            if current_node.previous not in seen:
                seen[current_node.previous] = Node(current_node.previous.key)
            current_clone_node.previous = seen[current_node.previous]
        current_node = current_node.next
    return clone

