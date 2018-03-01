"""Check if a linked list is a palindrome."""

from linked_list import *

def linked_list_to_array(linked_list):
    array = []
    pos = 1
    node = linked_list.get_position(pos)
    while node:
        array.append(node)
        pos += 1
        node = linked_list.get_position(pos)
    return array

def is_palindrome(array):
    if len(array) <= 1:
        return True
    return array[0].key == array[-1].key and is_palindrome(array[1:-1])


if __name__ == "__main__":
    # Initialize a LinkedList with a head that has key 1
    linked_list = LinkedList(Node(1))
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    print (is_palindrome(linked_list_to_array(linked_list)))