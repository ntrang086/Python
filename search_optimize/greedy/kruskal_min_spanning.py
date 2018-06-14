"""A minimum spanning tree (MST) of a weighted, connected and undirected graph
is a spanning tree with weight less than or equal to the weight of every other
spanning tree. The weight of a spanning tree is the sum of weights given to 
each edge of the spanning tree.
Find a MST using Kruskal's algorithm
"""
import sys
from heapq import *

class Graph(object):
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = []

    def add_edge(self, node_1, node_2, weight):
        self.graph.append((node_1, node_2, weight))

    def find(self, parent, i):
        """Follow the chain of parent pointers from x until it reaches a root
        element, whose parent is itself. This root element is the representative
        member of the set to which x belongs, and may be x itself."""
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """Use find() to determine the roots of the trees x and y belong to. If
        the roots are distinct, the trees are combined by attaching the shorter
        tree to the root of the taller tree.
        """
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if x_root == y_root:
            return
        # x and y are not in same set, so we lower-rank tree to higher-rank one
        if rank[x_root] < rank[y_root]:
            x_root, y_root = y_root, x_root
        parent[y_root] = x_root
        # If ranks are the same we increment rank of the final tree
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1

    def is_cyclic_union_find(self):
        """Detect cycle in a graph."""
        # For each node, initialize its parent as itself and its rank as 0
        parent = []
        rank = []
        for i in range(self.num_nodes):
            parent.append(i)
            rank.append(0)
        # Find the parent of both nodes of each edge
        # If both subsets are the same, there is cycle in graph.
        for i, j, w in self.graph:
            x = self.find(parent, i)
            y = self.find(parent, j)
            if x == y:
                return True
            self.union(parent, rank, x, y)
        return False

    def kruskal_MST(self):
        """Steps:
        1. Sort all the edges in non-decreasing order of their weight.
        2. Pick the smallest edge. Check if it forms a cycle with the spanning tree 
        formed so far. If cycle is not formed, include this edge. Else, discard it.
        3. Repeat step#2 until there are (V-1) edges in the spanning tree.
        """
        result = []
        # For each node, initialize its parent as itself and its rank as 0
        parent = []
        rank = []
        for i in range(self.num_nodes):
            parent.append(i)
            rank.append(0)
        # Sort all the edges in non-decreasing order of their weight
        sorted_graph = sorted(self.graph, key=lambda x:x[2])
        # Index of edges in sorted_graph
        edge_i = 0
        # Count the number of edges in the current spannning tree
        edge_count = 0
        while edge_count < self.num_nodes - 1:
            i, j, w = sorted_graph[edge_i]
            edge_i += 1
            x = self.find(parent, i)
            y = self.find(parent, j)
            if x != y:
                result.append((i, j, w))
                edge_count += 1
                self.union(parent, rank, x, y)
        return result

    def clear(self):
        """Clear all nodes and edges. Otherwise, when creating a new graph, the
        nodes and edges of an old graph may be added to the new one.
        """
        self.graph.clear()

if __name__ == "__main__":
    # Test cycle detections
    g = Graph(3)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 1)
    assert g.is_cyclic_union_find() == False
    g.add_edge(2, 0, 1)
    assert g.is_cyclic_union_find() == True
    g.clear()
    g = Graph(5)
    g.add_edge(1, 0, 1)
    g.add_edge(0, 2, 1)
    g.add_edge(2, 0, 1)
    g.add_edge(0, 3, 1)
    g.add_edge(3, 4, 1)
    assert g.is_cyclic_union_find() == True
    g.clear()

    # Test Kruskal MST algorithm
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
     
    assert g.kruskal_MST() == [(2, 3, 4), (0, 3, 5), (0, 1, 10)]