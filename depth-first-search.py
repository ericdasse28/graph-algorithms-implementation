"""
Python3 program to print DFS traversal
from a given graph
"""
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation


class Graph:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Function to add an edge"""
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        """A function used by DFS"""

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=" ")

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, v):
        """The function to do DFS traversal. It uses
        recursive dfs_util()"""

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.dfs_util(v, visited)


# Driver code

# Create a graph given
# in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(2)
