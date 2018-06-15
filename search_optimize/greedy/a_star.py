"""Given a graph, a source node and a goal node in the graph, find the lowest
cost path from the source to the goal using A* algorithm.
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

    def heuristic_cost_estimate(self, current, goal):
        """A very simple heuristic cost function."""
        return goal - current
        
    def a_star(self, start, goal):
        """Find the shortest path from start node to goal node.
        We use a binary min heap to find the next node with min total cost.
        """
        # Keep track of visited and unvisited nodes
        visited = set()
        unvisited = []
        # For each node, which node it can most efficiently be reached from.
        # If a node can be reached from many nodes, came_from will eventually contain the
        # most efficient previous step.
        came_from = dict()
        # For each node, the cost of getting from the start node to that node.
        g_score = [sys.maxsize for i in range(self.num_nodes)]
        g_score[start] = 0
        # For each node, the total cost of getting from the start node to the goal
        # by passing by that node. That value is partly known, partly heuristic.
        f_score = [sys.maxsize for i in range(self.num_nodes)]
        f_score[start] = self.heuristic_cost_estimate(start, goal)
        heappush(unvisited, (f_score[start], start))
        while unvisited:
            min_d, min_node = heappop(unvisited)
            if min_node == goal:
                return self.reconstruct_path(came_from, min_node)
            if min_node not in visited:
                visited.add(min_node)
                for neighbor, weight in self.graph[min_node]:
                    if g_score[neighbor] > weight + g_score[min_node]:
                        came_from[neighbor] = min_node
                        g_score[neighbor] = weight + g_score[min_node]
                        f_score[neighbor] = g_score[neighbor] + self.heuristic_cost_estimate(neighbor, goal)
                        heappush(unvisited, (f_score[neighbor], neighbor))
        # There is no path from start to goal
        return -1, -1

    def reconstruct_path(self, came_from, current):
        """Reconstruct the path from the current node to the past nodes."""
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path

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
    print(g.a_star(0, 6))
    g.clear()