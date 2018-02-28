"""Implement a queue."""

import sys
sys.path.append("../linked_list")
from linked_list import Node

class Queue():
    def __init__(self, max_size=sys.maxsize):
        """Initialize a Queue
        Parameters:
        max_size: max number of nodes in the queue
        num_nodes: number of nodes in the queue
        front: points the first item of queue
        rear: points to last item of queue
        """
        self.max_size = max_size
        self.num_nodes = 0
        self.front = None
        self.rear = None
    
    def queue(self, key):
        """Add a key to the queue."""
        new_node = Node(key)
        if self.num_nodes == self.max_size:
            print ("Queue overflow")
        elif self.rear is None:
            self.front = new_node
            self.rear = new_node
            self.num_nodes += 1
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.num_nodes += 1
    
    def dequeue(self):
        """Remove the first key."""
        if self.front is None:
            return None
        deleted_node = self.front
        self.front = self.front.next
        self.num_nodes -= 1
        # If queue becomes empty, change rear to None
        if self.front.next is None:
            self.rear = None
        return deleted_node


if __name__ == "__main__":
    # Initialize a queue
    queue = Queue()
    queue.queue(1)
    queue.queue(2)
    queue.queue(3)

    # Should print 3
    print (queue.num_nodes)
    # Should print 1
    print (queue.dequeue().key)
    # Should print 2
    print (queue.dequeue().key)
    # Should print 1
    print (queue.num_nodes)
