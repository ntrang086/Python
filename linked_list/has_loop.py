"""Check if a linked list has a loop.
Find the node at the beginning of the loop."""

from linked_list import *

def has_loop(linked_list):
    """Check if a linked list has a loop"""
    seen_nodes = set()
    current_node = linked_list.head
    while current_node:
        if current_node in seen_nodes:
            return True
        seen_nodes.add(current_node)
        current_node = current_node.next
    return False

def find_loop_start(linked_list):
    """Find the start node of a loop"""
    seen_nodes = set()
    current_node = linked_list.head
    while current_node:
        if current_node in seen_nodes:
            return current_node
        seen_nodes.add(current_node)
        current_node = current_node.next
    return None

def find_loop_start2(linked_list):
    """Find the start node of a loop based on Floyd's tortoise 
    and hare algorithm. Assume that head is at position 1."""
    
    has_loop = False
    # Tortoise starts at the position next to head
    tortoise_pos = 2
    # Hare starts at the position next to tortoise
    hare_pos = tortoise_pos + 1
    tortoise_node = linked_list.get_position(tortoise_pos)
    hare_node = linked_list.get_position(hare_pos)
    while tortoise_node and hare_node:
        if tortoise_node.key == hare_node.key:
            has_loop = True
            break
        # Hare moves twice as fast as tortoise
        tortoise_pos += 1
        hare_pos += 2
        tortoise_node = linked_list.get_position(tortoise_pos)
        hare_node = linked_list.get_position(hare_pos)
    
    if has_loop == False:
        return None, 0
    # Find the index of the first node of the loop
    loop_start_pos = 1
    tortoise_pos = 1
    tortoise_node = linked_list.get_position(tortoise_pos)
    while tortoise_node and hare_node:
        if tortoise_node.key == hare_node.key:
            break
        loop_start_pos += 1
        # Tortoise and hare move at the same speed
        tortoise_pos += 1
        hare_pos += 1
        tortoise_node = linked_list.get_position(tortoise_pos)
        hare_node = linked_list.get_position(hare_pos)

    # (Optional) Find the length of the loop
    # Freeze tortoise and move hare until hare points to the same
    # node as tortoise
    loop_length = 1
    hare_pos = tortoise_pos + 1
    hare_node = linked_list.get_position(hare_pos)
    while hare_node:
        if tortoise_node.key == hare_node.key:
            break
        hare_pos += 1
        hare_node = linked_list.get_position(hare_pos)
        loop_length += 1
    return linked_list.get_position(loop_start_pos), loop_length

if __name__ == "__main__":
    # Initialize a LinkedList with a head that has key 1
    linked_list = LinkedList(Node(1))
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    node_5 = linked_list.get_position(5)
    node_5.next = linked_list.get_position(2)
    print (has_loop(linked_list))
    start_node, loop_length = find_loop_start2(linked_list)
    print (start_node.key, loop_length)