# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist):
        print("Vertex \tDistance from source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def min_distance(self, dist, spt_set):
        """
        A utility function to find the vertex with
        minimum distance value, from the set of vertices
        not yet included in shortest path tree
        """
        # Initialize minimum distance for next node
        min_dist = sys.maxint

        # Search for nearest vertex not in
        # the shortest path tree
        for u in range(self.V):
            if dist[u] < min_dist and spt_set[u] is False:
                min_dist = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):
        """
        Function that implements Dijkstra's single source
        shortest path algorithm for a graph represented
        using adjacency matrix representation
        """

        dist = [sys.maxint] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for cost in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.min_distance(dist, spt_set)

            # Put the minimum distance vertex in the
            # shortest path tree
            spt_set[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex is not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and spt_set[y] is False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.print_solution(dist)


# Driver program
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

g.dijkstra(0)
