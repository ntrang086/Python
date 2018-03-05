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

    def append(self, key):
        """Append the key to the end of the list"""
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.previous = current_node
    
    def delete(self, key):
        """Delete a node with a specified key and return the node.
        Return None if the key is not in the list"""
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.key == key:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.previous = previous_node
                return current_node
            previous_node = current_node
            current_node = current_node.next
        return current_node

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print (current_node.key)
            current_node = current_node.next


if __name__ == "__main__":
    # Initialize a DoublyLinkedList with a head that has key 2
    doubly_linked_list = DoublyLinkedList(Node(2))
    doubly_linked_list.insert_front(1)
    doubly_linked_list.insert_after(4, doubly_linked_list.head.next)
    doubly_linked_list.insert_before(3, doubly_linked_list.head.next)
    
    # Should print 1, 2, 3, and 4 respectively
    doubly_linked_list.print_linked_list()