"""Implement a doubly LinkedList."""

class Node():
    def __init__(self, key):
        self.key = key
        self.previous = None
        self.next = None

class DoublyLinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert_front(self, key):
        """Insert a key at the front"""
        new_node = Node(key)
        if self.head:
            self.head.previous = new_node
            new_node.next = self.head
        self.head = new_node

