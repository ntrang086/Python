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


if __name__ == "__main__":
    # Initialize a randomly linked list with a head that has key 1
    rand_linked_list = DoublyLinkedList(Node(1))
    rand_linked_list.append(2)
    rand_linked_list.append(3)
    rand_linked_list.append(4)
    rand_linked_list.append(5)

    # Assign the head's previous pointer to 3
    rand_linked_list.head.previous = rand_linked_list.head.next.next
    # Append node 3's previous pointer to 5
    rand_linked_list.head.next.next.previous = rand_linked_list.head.next.next.next.next
    # Assign node 5's previous pointer to 2 
    rand_linked_list.head.next.next.next.next.previous = rand_linked_list.head.next
    
    clone = clone_linked_list(rand_linked_list)
    # Should print 1, 2, 3, 4 and 5 respectively
    clone.print_linked_list()
    # Should print 3
    print (clone.head.previous.key)
    # Should print 5
    print (clone.head.next.next.previous.key)
    # Should print 2
    print (clone.head.next.next.next.next.previous.key)
