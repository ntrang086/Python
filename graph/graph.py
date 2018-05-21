"""Create a directed graph that has nodes and edges. The Graph class has
functions that return various representations of the same graph."""

from collections import deque
from copy import deepcopy

class Node(object):
    """A node has a value and a list of edges that start or end with it."""

    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    """An edge has a value and a direction: the start node and the end node."""
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    """A directed graph contains a list of vertexes and edges. It may have
    cycles. It has functions to insert/delete a node or an edge, return various
    representations and traverse the nodes. Assume that each node has a unique
    value, but edges do not have to.
    """

    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def search_node(self, node_val):
        for node in self.nodes:
            if node.value == node_val:
                return node
        return None

    def insert_node(self, new_node_val):
        """Insert a node with new_node_val."""
        if self.search_node(new_node_val):
            print ("A node with this value already exists.")
            return
        self.nodes.append(Node(new_node_val))

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        """Insert an edge with new_edge_val, starting from node_from_val and
        endinng with node_to_val."""
        node_from = self.search_node(node_from_val)
        node_to = self.search_node(node_to_val)
        # If node_from is not present in the graph
        if node_from is None:
            node_from = Node(node_from_val)
            self.nodes.append(node_from)
        # If node_to is not present in the graph
        if node_to is None:
            node_to = Node(node_to_val)
            self.nodes.append(node_to)
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Return a list of triples that store an edge's value, "from" node and
        "to" node: [(Edge Value, From Node Value, To Node Value), ...].
        """
        return [(edge.value, edge.node_from.value, edge.node_to.value) 
                for edge in self.edges]

    def get_adjacency_list(self):
        """Return a list of lists: The indicies of the outer list represent
        "from" nodes. Each sublist can be None or store a list of tuples:
        [[(To Node, Edge Value), (To Node, Edge Value), ...], None, ...].
        """
        max_index = max(node.value for node in self.nodes)
        adjacency_list = [None] * (max_index + 1)
        for edge in self.edges:
            index = edge.node_from.value
            if adjacency_list[index] is None:
                adjacency_list[index] = []
            adjacency_list[index].append((edge.node_to.value, edge.value))
        return adjacency_list

    def get_adjacency_matrix(self):
        """Return a matrix: Rows represent "from" nodes; columns represent "to"
        nodes. Store an edge value in each spot, or a 0 if no edge exists.
        """
        max_index = max(node.value for node in self.nodes)
        # Initialize a matrix. Note that we can't use * for for the outer list,
        # i.e. [[0] * (max_index + 1) * (max_index + 1),] because this will create a list containing (max_index + 1) 
        # references to the same sublist.
        adjacency_matrix = [[0] * (max_index + 1) for i in range((max_index + 1))]
        for edge in self.edges:
            adjacency_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return adjacency_matrix

    def breadth_first_traversal(self, node_val):
        """Traverse the graph in breadth-first order starting from node_val."""
        # Keep track of nodes that we have seen
        seen = set()
        # A queue to store the frontier nodes to traverse
        queue = deque()
        result = []
        start_node = self.search_node(node_val)
        if start_node:
            queue.append(start_node)
            seen.add(start_node)
        while queue:
            node = queue.popleft()
            result.append(node.value)
            for edge in node.edges:
                # If the node of interest is the start of an edge
                next_node = edge.node_to
                if next_node not in seen:
                    queue.append(next_node)
                    seen.add(next_node)
        return result

    def level_BFS(self, root):
        current_level = {root}
        seen = set()
        l = 0
        while True:
            print (l, [node.value for node in current_level])
            seen.update(current_level)
            next_level = set()
            for node in current_level:
                for edge in node.edges:
                    if edge.node_to not in seen:
                        next_level.add(edge.node_to)
            if len(next_level) == 0:
                return
            current_level = next_level.copy()
            l += 1
    
    def depth_first_traversal(self, node_val):
        """Traverse the graph in depth-first order starting from node_val."""
        return self._depth_first_traversal_util(node_val, set(), [])

    def _depth_first_traversal_util(self, node_val, seen, result):
        node = self.search_node(node_val)
        if node:
            result.append(node.value)
            seen.add(node_val)
        for edge in node.edges:
            next_node = edge.node_to
            if next_node.value not in seen:
                self._depth_first_traversal_util(next_node.value, seen, result)
        return result

    def depth_first_traversal_iterative(self, node_val):
        seen = set()
        stack = []
        result = []
        node = self.search_node(node_val)
        if node:
            stack.append(node)
        while stack:
            node = stack.pop()
            if node not in seen:
                result.append(node.value)
                seen.add(node)
            for edge in node.edges:
                if edge.node_to not in seen:
                    stack.append(edge.node_to)
        return result

    def _update_transitive_row(self, node_val, seen, transitive_row):
        """Depth-first search helper function for transitive_closure. Traverse
        the graph from node_val and update the transitive_matrix accordingly.
        """
        node = self.search_node(node_val)
        if node:
            seen.add(node_val)
            for edge in node.edges:
                next_node = edge.node_to
                transitive_row[next_node.value] = 1
                # If all the cells of the row have been updated, move on to next row
                if sum(transitive_row) == len(transitive_row):
                    break
                if next_node.value not in seen:
                    self._update_transitive_row(next_node.value, seen, transitive_row)
        return transitive_row

    def transitive_closure(self):
        """Find the transitive closure matrix using DFS. Rows represent "from"
        nodes, and columns "to" nodes. If a cell has value of 1, there's a path
        between "from" and "to" nodes; if 0, there is no path.
        """
        max_index = max(node.value for node in self.nodes)
        transitive_matrix = [[0] * (max_index + 1) for i in range((max_index + 1))]
        for i in range(max_index + 1):
            transitive_matrix[i] = self._update_transitive_row(i, set(), transitive_matrix[i])
        return transitive_matrix

    def find_all_paths(self, node_1, node_2):
        """Find all possible paths between node_1 and node_2."""
        paths = []
        self._find_all_paths_util(node_1, node_2, set(), [], paths)
        return paths

    def _find_all_paths_util(self, node_1, node_2, seen, path, paths):
        """Helper function for find_all_paths."""
        seen.add(node_1)
        path.append(node_1)
        if node_1 is node_2:
            # Make a copy of path so that any update on it won't affect paths
            paths.append(deepcopy(path))
        else:
            for edge in node_1.edges:
                if edge.node_to not in seen:
                    self._find_all_paths_util(edge.node_to, node_2, seen, path, paths)
        path.pop()
        seen.remove(node_1)

    def count_all_paths(self, node_1, node_2):
        """Count all paths between two nodes."""
        return self._count_all_paths_util(node_1, node_2, set(), 0)

    def _count_all_paths_util(self, node_1, node_2, seen, count):
        """Helper function for count_all_paths."""
        seen.add(node_1)
        if node_1 is node_2:
            count += 1
        else:
            for edge in node_1.edges:
                if edge.node_to not in seen:
                    count = self._count_all_paths_util(edge.node_to, node_2, seen, count)
        seen.remove(node_1)
        return count

    def clear(self):
        """Clear all nodes and edges. Otherwise, when creating a new graph, the
        nodes and edges of an old graph may be added to the new one.
        """
        self.nodes.clear()
        self.edges.clear()


if __name__ == "__main__":
    # Initialize a Graph and add edges
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)

    # Test the graph representation functions
    assert graph.get_edge_list() == [(100, 1, 2), (101, 1, 3), 
                                     (102, 1, 4), (103, 3, 4)]
    assert graph.get_adjacency_list() == [None, [(2, 100), (3, 101), (4, 102)],
                                          None, [(4, 103)], None]
    assert graph.get_adjacency_matrix() == [[0, 0, 0, 0, 0], 
                                            [0, 0, 100, 101, 102], 
                                            [0, 0, 0, 0, 0], 
                                            [0, 0, 0, 0, 103], 
                                            [0, 0, 0, 0, 0]]
    # Test breadth-first traversal
    assert graph.breadth_first_traversal(1) == [1, 2, 3, 4]
    # Add a cycle for node 2
    graph.insert_edge(100, 2, 2)
    assert graph.breadth_first_traversal(1) == [1, 2, 3, 4]

    # Test depth-first traversal
    assert graph.depth_first_traversal(1) == [1, 2, 3, 4]
    assert graph.depth_first_traversal_iterative(1) == [1, 4, 3, 2]
    graph.level_BFS(graph.nodes[0])
    
    graph.clear()

    # Create another graph
    graph_2 = Graph()
    graph_2.insert_edge(1, 0, 1)
    graph_2.insert_edge(1, 0, 2)
    graph_2.insert_edge(1, 1, 2)
    graph_2.insert_edge(1, 2, 0)
    graph_2.insert_edge(1, 2, 3)
    graph_2.insert_edge(1, 3, 3)

    # Test breadth-first traversal
    assert graph_2.breadth_first_traversal(2) == [2, 0, 3, 1]
    # Test depth-first traversal
    assert graph_2.depth_first_traversal(2) == [2, 0, 1, 3]
    # Test transitive closure
    assert graph_2.transitive_closure() == [[1, 1, 1, 1],
                                            [1, 1, 1, 1],
                                            [1, 1, 1, 1],
                                            [0, 0, 0, 1]]

    assert graph_2.depth_first_traversal_iterative(0) == [0, 2, 3, 1]
    node_0_to_3 = graph_2.find_all_paths(graph_2.nodes[0], graph_2.nodes[3])
    assert [[node.value for node in path] for path in node_0_to_3]  \
           == [[0, 1, 2, 3], [0, 2, 3]]
    assert graph.count_all_paths(graph_2.nodes[0], graph_2.nodes[3]) == 2
    graph_2.clear()
