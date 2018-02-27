"""Implement a stack using a LinkedList.
The stack has push and pop functions."""

import sys
sys.path.append("../linked_list")
from linked_list import LinkedList, Node

class Stack():
    def __init__(self, max_size=sys.maxsize, top=None):
        self.max_size = max_size
        self.linked_list = LinkedList(top)
        if top is None:
            self.num_nodes = 0
        else:
            self.num_nodes = 1
    
    def push(self, key):
        """Insert a key on top of a stack."""
        if self.num_nodes == self.max_size:
            print ("Stack overflow")
        else:
            self.linked_list.insert(key, 1)
            self.num_nodes += 1
    
    def pop(self):
        """Remove the top key."""
        deleted_node = self.linked_list.delete_head()
        if deleted_node:
            self.num_nodes -= 1
        return deleted_node


if __name__ == "__main__":
    # Initialize a stack with a node
    stack = Stack(top=Node(1))

    # Test stack functionality
    stack.push(2)
    stack.push(3)
    print (stack.num_nodes)
    
    print (stack.pop().key)
    print (stack.pop().key)
    print (stack.pop().key)
    print (stack.pop())
    stack.push(4)
    print (stack.num_nodes)
    print (stack.pop().key)