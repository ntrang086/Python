"""You are given a m litre jug and a n litre jug . Both the jugs are initially
empty. The jugs don’t have markings to allow measuring smaller quantities. You
have to use the jugs to measure d litres of water where d is less than n.
(X, Y) corresponds to a state where X refers to amount of water in Jug1 and Y
refers to amount of water in Jug2. 

Determine the path from initial state (xi, yi) to final state (xf, yf), where
(xi, yi) is (0, 0) which indicates both jugs are initially empty and (xf, yf)
indicates a state which could be (0, d) or (d, 0).

The operations you can perform are:
- Empty a Jug: (X, Y)->(0, Y) Empty Jug 1
- Fill a Jug: (0, 0)->(X, 0) Fill Jug 1
- Pour water from one jug to the other until one of the jugs is either empty or
full: (X, Y) -> (X-d, Y+d)
Examples:
Input : 4 3 2
Output : [(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2)]
"""

from collections import deque
from copy import deepcopy

def get_next_states(state, jug_1_cap, jug_2_cap):
    """Return the next states from the current state."""
    next_states = set()
    total = sum(state)
    # If there is water in jug 1, empty it
    if state[0] > 0:
        next_states.add((0, state[1]))
    # If there is water in jug 2, empty it
    if state[1] > 0:
        next_states.add((state[0], 0))
    # If water in jug 1 is less than capacity
    if state[0] < jug_1_cap:
        # Fill jug 1
        next_states.add((jug_1_cap, state[1]))
        # If there is water in jug 2, pour water from jug 2 to 1
        if state[1] > 0:
            next_states.add((min(total, jug_1_cap),
                             max(0, total - jug_1_cap)))
    # If water in jug 2 is less than capacity
    if state[1] < jug_2_cap:
        # Fill jug 2
        next_states.add((state[0], jug_2_cap))
        # If there is water in jug 1, pour water from jug 1 to 2
        if state[0] > 0:
            next_states.add((max(0, total - jug_2_cap), 
                             min(total, jug_2_cap)))
    return next_states

def water_jug_one_path(jug_1_cap, jug_2_cap, d):
    """From the initial state (0, 0) where both jugs are empty, find a path
    to the goal state. The goal here is to measure a d amount of water. 
    In other words, the goal state is either (0, d) or (d, 0).
    """
    # Keep track of seen states. Initially, the jugs are empty
    return _water_jug_one_path_util((0, 0), d, jug_1_cap, jug_2_cap, set(), [])
    
def _water_jug_one_path_util(curr_state, d, jug_1_cap, jug_2_cap, seen, result):
    seen.add(curr_state)
    result.append(curr_state)
    if curr_state == (0, d) or curr_state == (d, 0):
        return result
    next_states = get_next_states(curr_state, jug_1_cap, jug_2_cap)
    for state in next_states:
        if state not in seen:
            return _water_jug_one_path_util(state, d, jug_1_cap, jug_2_cap, seen, result)


def water_jug_all_paths(jug_1_cap, jug_2_cap, d):
    """From the initial state (0, 0) where both jugs are empty, find all paths
    to the goal state. The goal here is to measure a d amount of water. 
    In other words, the goal state is either (0, d) or (d, 0).
    """
    # Keep track of seen states. Initially, the jugs are empty
    paths = []
    _water_jug_all_paths_util((0, 0), d, jug_1_cap, jug_2_cap, set(), [], paths)
    return paths
    
def _water_jug_all_paths_util(curr_state, d, jug_1_cap, jug_2_cap, seen, path, paths):
    seen.add(curr_state)
    path.append(curr_state)
    if curr_state == (0, d) or curr_state == (d, 0):
        paths.append(deepcopy(path))
    next_states = get_next_states(curr_state, jug_1_cap, jug_2_cap)
    for state in next_states:
        if state not in seen:
            _water_jug_all_paths_util(state, d, jug_1_cap, jug_2_cap, seen, path, paths)
    path.pop()
    seen.remove(curr_state)


if __name__ == "__main__":
    # Test get_next_states
    assert get_next_states((0, 0), 4, 3) == {(0, 3), (4, 0)}
    assert get_next_states((0, 3), 4, 3) == {(0, 0), (3, 0), (4, 3)}
    assert get_next_states((4, 0), 4, 3) == {(0, 0), (1, 3), (4, 3)}
    assert get_next_states((4, 3), 4, 3) == {(0, 3), (4, 0)}

    print (water_jug_one_path(4, 3, 2))
    print (water_jug_all_paths(4, 3, 2))