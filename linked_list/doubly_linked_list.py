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

    def insert_after(self, key, previous_node):
        """Insert a key after a specified node.
        Do nothing if node is None"""
        new_node = Node(key)
        if previous_node is None:
            print ("Previous node is None. Did nothing.")
            return        
        new_node.previous = previous_node
        new_node.next = previous_node.next
        previous_node.next = new_node
        if new_node.next:
            new_node.next.previous = new_node

    def insert_before(self, key, next_node):
        """Insert a key before a specified node.
        Do nothing if node is None"""
        new_node = Node(key)
        if next_node is None:
            print ("Next node is None. Did nothing.")
            return        
        new_node.previous = next_node.previous
        new_node.next = next_node
        next_node.previous = new_node
        if new_node.previous:
            new_node.previous.next = new_node

