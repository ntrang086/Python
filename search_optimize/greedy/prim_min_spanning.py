"""A minimum spanning tree (MST) of a weighted, connected and undirected graph
is a spanning tree with weight less than or equal to the weight of every other
spanning tree. The weight of a spanning tree is the sum of weights given to 
each edge of the spanning tree.
Find a MST using Prim's algorithm.
"""
from collections import defaultdict
import sys
from heapq import *

class Graph(object):
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = defaultdict(list)

    def add_edge(self, node_1, node_2, weight):
        self.graph[node_1].append((node_2, weight))
        self.graph[node_2].append((node_1, weight))
    
    def prim_MST(self, start_node):
        """Find a MST using Prim's algorithm."""
        # Keep track of nodes included in the min spanning tree & their weights
        min_spanning_tree = [-1 for i in range(self.num_nodes)]
        # Keep track of visited and unvisited nodes
        visited = set()
        unvisited = []
        heappush(unvisited, (0, start_node))
        # Cost of a connection to each node, initially infinity
        cost = [sys.maxsize for i in range(self.num_nodes)]
        cost[start_node] = 0
        while unvisited:
            min_d, min_node = heappop(unvisited)
            if min_node not in visited:
                visited.add(min_node)
                for neighbor, weight in self.graph[min_node]:
                    if neighbor not in visited and cost[neighbor] > weight:
                        cost[neighbor] = weight
                        heappush(unvisited, (cost[neighbor], neighbor))
                        min_spanning_tree[neighbor] = (min_node, weight)
        return min_spanning_tree

    def print_prim_MST(self, min_spanning_tree, n):
        """Print Prim MST nodes and weights."""
        for i in range(1, n):
            print ("%d - %d: %d" % (min_spanning_tree[i][0], i, min_spanning_tree[i][1]))
    
    def clear(self):
        """Clear all nodes and edges. Otherwise, when creating a new graph, the
        nodes and edges of an old graph may be added to the new one.
        """
        self.graph.clear()

if __name__ == "__main__":
    g = Graph(9)
    # List of edges, each containing the start node, end node and weight
    edges = [(0, 1, 4),
            (0, 7, 8),
            (1, 2, 8),
            (1, 7, 11),
            (2, 3, 7),
            (2, 8, 2),
            (2, 5, 4),
            (3, 4, 9),
            (3, 5, 14),
            (4, 5, 10),
            (5, 6, 2),
            (6, 7, 1),
            (6, 8, 6),
            (7, 8, 7)]
    for edge in edges:
        g.add_edge(edge[0], edge[1], edge[2])
    mst = g.prim_MST(0)
    g.print_prim_MST(mst, g.num_nodes)
    g.clear()