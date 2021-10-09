# Python3 Program to print BFS traversal
# from a given source vertex. BFS (int s)
# traverses vertices reachable from s
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation


class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def bfs(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        # Mark the source node as
        # visited and enqueue it
        queue = [s]
        visited[s] = True

        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If an adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Driver code


# Creation of a graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2")
g.bfs(2)
