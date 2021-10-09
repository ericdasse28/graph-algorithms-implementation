"""
Python program to do a DFS traversal for a complete graph

The code to traverse graphs in the depth-first-search module traverses only
the vertices reachable from a given source vertex. All the vertices may not
be reachable from a given vertex, as in a Disconnected graph. To do a complete
DFS traversal of such graphs, run DFS from all unvisited nodes after a DFS
"""
from collections import defaultdict


class Graph:
    """This class represents a directed graph using
    adjacency list comprehension"""

    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        if v is None:
            self.graph[u] = []
        else:
            self.graph[u].append(v)

    def dfs_util(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self):
        # Create a set to store all visited vertices
        visited = set()

        # Call the recursive helper function to print DFS traversal starting
        # from all vertices one by one

        # Copy the keys to a list to avoid
        # RunTimeError: dictionary changed size during iteration
        # while performing DFS from each individual node
        keys = list(self.graph.keys())

        for vertex in keys:
            if vertex not in visited:
                self.dfs_util(vertex, visited)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.add_edge(8, 9)
g.add_edge(7, None)
g.dfs()
