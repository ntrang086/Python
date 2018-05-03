"""Create a directed graph that has nodes and edges. The Graph class has
functions that return various representations of the same graph."""


class Node(object):
    """A node has a value and a list of edges that start or end with it."""

    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    """An edge has a value and a direction: the start node the end node."""
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    """A graph contains a list of vertexes and edges. It has functions to
    insert/delete a node or an edge and to return various representations.
    Assume that each node has a unique value, but edges do not have to."""

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

    def get_node_list(self):
        """Return a list of node values"""
        return [node.value for node in self.nodes]
    
    def get_edge_list(self):
        """Return a list of triples that store an edge's value, "from" node and
        "to" node: [(Edge Value, From Node Value, To Node Value), ...]"""
        return [(edge.value, edge.node_from.value, edge.node_to.value) 
                for edge in self.edges]

    def get_adjacency_list(self):
        """Return a list of lists: The indicies of the outer list represent
        "from" nodes. Each sublist can be None or store a list of tuples:
        [[(To Node, Edge Value), (To Node, Edge Value), ...], None, ...]"""
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
        nodes. Store an edge value in each spot, or a 0 if no edge exists."""
        max_index = max(node.value for node in self.nodes)
        # Initialize a matrix. Note that we can't use * for to create a list of
        # sublists because this will create a list containing (max_index + 1) 
        # references to the same sublist.
        adjacency_matrix = [[0] * (max_index + 1) for i in range((max_index + 1))]
        for edge in self.edges:
            adjacency_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return adjacency_matrix


if __name__ == "__main__":
    # Initialize a Graph and add edges
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)

    # Test the functions of Graph
    assert graph.get_node_list() == [1, 2, 3, 4]
    assert graph.get_edge_list() == [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    assert graph.get_adjacency_list() == [None, [(2, 100), (3, 101), (4, 102)], None, 
                                          [(4, 103)], None]
    assert graph.get_adjacency_matrix() == [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], 
                                            [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]