"""Implement LinkedList."""

class Node():
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, key):
        """Append the key to the end of the list"""
        if self.head is None:
            self.head = Node(key)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(key)

    def insert(self, key, position):
        """Insert a key at a specified position. Assume head is
        at position 1. If position is greater than the length of
        the list, append the key to the end"""
        new_node = Node(key)
        count = 1
        if position == 1 or self.head is None:
            new_node.next = self.head
            self.head = new_node
        elif position > 1:
            current_node = self.head
            previous_node = None
            while current_node and count < position:
                previous_node = current_node
                current_node = current_node.next
                count += 1
            previous_node.next = new_node
            new_node.next = current_node
    
    def delete(self, key):
        """Delete a node with a specified key and return the node.
        Return None if the key is not in the list"""
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.key == key:
                # If the key to be deleted is not the head
                if previous_node:
                    previous_node.next = current_node.next
                # If the key to be deleted is the head
                else:
                    self.head = current_node.next
                return current_node
            previous_node = current_node
            current_node = current_node.next
        return current_node

    def delete_head(self):
        """Delete the head node."""
        deleted_node = self.head
        if deleted_node:
            self.head = self.head.next
        return deleted_node

    def delete_position(self, position):
        """Delete a node at a specified position. Return the deleted
        node or None if position is grater than the length of list"""
        if position < 1 or self.head is None:
            return None
        if position == 1:
            return self.delete_head()
        current_node = self.head
        previous_node = None
        current_pos = 1
        while current_pos < position and current_node:
            previous_node = current_node
            current_node = current_node.next
            current_pos += 1
        if current_node:
            previous_node.next = current_node.next
        return current_node

    def get_position(self, position):
        """Return a node from the specified position. Assume head is
        at position 1. Return None if position is greater than the length
        of list."""
        if position < 1:
            return None
        if self.head:
            current_pos = 1
            current_node = self.head
            while current_pos < position and current_node:
                current_node = current_node.next
                current_pos += 1
            return current_node
        return None

if __name__ == "__main__":
    # Initialize a LinkedList with a head that has key 1
    linked_list = LinkedList(Node(1))
    linked_list.append(2)
    linked_list.append(3)

    # Test get_position
    # Should print 3
    print (linked_list.head.next.next.key)
    # Should also print 3
    print (linked_list.get_position(3).key)

    # Test insert
    linked_list.insert(4, 3)
    # Should print 4 
    print (linked_list.get_position(3).key)

    # Test delete
    linked_list.delete(1)
    # Should print 2 
    print (linked_list.get_position(1).key)
    # Should print 4 
    print (linked_list.get_position(2).key)
    # Should print 3 
    print (linked_list.get_position(3).key)
    # Should print 3 
    print (linked_list.delete_position(3).key)
    # Should print None
    print (linked_list.get_position(3))