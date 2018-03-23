"""Given a singly linked list A->B->C->D->E->F... convert to B->A->D->C->F->E..."""

from linked_list import *

def reverse_pair(linked_list):
    current_pos = 1
    current_node = linked_list.head
    previous_node = None
    while current_node:
        if current_pos == 2:
            linked_list.head = current_node
        if previous_node:
            previous_node.next = current_node.next
        if current_pos % 2 == 0:
            current_node.next = previous_node
            current_node = previous_node.next
            if current_node is None or current_node.next is None:
                break
        else:
            previous_node = current_node
            current_node = current_node.next
        current_pos += 1
    return linked_list

if __name__ == "__main__":
    # Initialize a LinkedList with a head that has key 1
    linked_list = LinkedList(Node("A"))
    linked_list.append("B")
    linked_list.append("C")
    linked_list.append("D")
    linked_list.append("E")

    #linked_list.print_linked_list()
    reverse_pair(linked_list)
    linked_list.print_linked_list()