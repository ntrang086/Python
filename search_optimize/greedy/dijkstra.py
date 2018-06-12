"""Given a graph and a source vertex in the graph, find shortest paths from
source to all nodes in the given graph using Dijsktra's algorithm.
We use adjacency list representation of a graph.
O(V) inserts into priority queue
O(V) EXTRACT MIN operations
O(E) DECREASE KEY operations
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

    def min_distance(self, dist, visited):
        """Helper function for dijkstra_all_nodes_array. Get the index of the
        min distance that is not in visited. This uses array implementation.
        """
        min_d = sys.maxsize
        min_node = 0
        for node in range(self.num_nodes):
            if dist[node] < min_d and node not in visited:
                min_d = dist[node]
                min_node = node
        return min_node

    def dijkstra_all_nodes_array(self, start_node):
        """Find the shortest path from start_node to each of the rest of nodes.
        We use array implementation to find the next node with min distance.
        O(V) time for extract min; O(1) for decrease key
        O(V*V + E*1) = O(V^2 + E) = O(V^2).
        """
        # Keep track of visited and unvisited nodes
        visited = set()
        unvisited = set()
        # Distances from start_node to nodes 
        dist = [sys.maxsize for i in range(self.num_nodes)]
        dist[start_node] = 0
        unvisited.add(start_node)
        while unvisited:
            min_node = self.min_distance(dist, visited)
            visited.add(min_node)
            unvisited.remove(min_node)
            for neighbor, weight in self.graph.get(min_node):
                if dist[neighbor] > weight + dist[min_node]:
                    dist[neighbor] = weight + dist[min_node]
                    unvisited.add(neighbor)
        return dist
    
    def dijkstra_all_nodes_heap(self, start_node):
        """Find the shortest path from start_node to each of the rest of nodes.
        We use a binary min heap to find the next node with min distance.
        O(lgV) for extract min; O(lgV) for decrease key
        O(VlgV + ElgV).
        """
        visited = set()
        unvisited = []
        heappush(unvisited, (0, start_node))
        # Distances from start_node to nodes 
        dist = [sys.maxsize for i in range(self.num_nodes)]
        dist[start_node] = 0
        while unvisited:
            min_d, min_node = heappop(unvisited)
            if min_node not in visited:
                visited.add(min_node)
                for neighbor, weight in self.graph.get(min_node):
                    if dist[neighbor] > weight + dist[min_node]:
                        dist[neighbor] = weight + dist[min_node]
                        heappush(unvisited, (dist[neighbor], neighbor))
        return dist
    
    def dijkstra_goal_node_heap(self, start_node, goal_node):
        """Find the shortest path from start_node to goal_node.
        We use a binary min heap to find the next node with min distance.
        """
        # Keep track of visited and unvisited nodes
        visited = set()
        unvisited = []
        heappush(unvisited, (0, start_node))
        # Distances from start_node to nodes 
        dist = [sys.maxsize for i in range(self.num_nodes)]
        dist[start_node] = 0
        while unvisited:
            min_d, min_node = heappop(unvisited)
            if min_node == goal_node:
                return dist[min_node]
            if min_node not in visited:
                visited.add(min_node)
                for neighbor, weight in self.graph.get(min_node):
                    if dist[neighbor] > weight + dist[min_node]:
                        dist[neighbor] = weight + dist[min_node]
                        heappush(unvisited, (dist[neighbor], neighbor))
        # There is no path from start_node to goal_node
        return -1

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

    assert g.dijkstra_all_nodes_array(0) == [0, 4, 12, 19, 21, 11, 9, 8, 14]
    assert g.dijkstra_all_nodes_heap(0) == [0, 4, 12, 19, 21, 11, 9, 8, 14]
    assert g.dijkstra_goal_node_heap(0, 0) == 0
    assert g.dijkstra_goal_node_heap(0, 4) == 21
    assert g.dijkstra_goal_node_heap(0, 8) == 14
    g.clear()