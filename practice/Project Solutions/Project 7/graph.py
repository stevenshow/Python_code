''' ADT to represent a weighted, directed graph
Instructor Solution
CS 2420 Project 7 Fall 2021

Original Author: Dana Doggett in 2019
Author: George Rudolph
Date: 25 Jun 2021
'''
import math

class Graph():
    ''' directed, weighted graph '''
    def __init__(self):
        self._vertices = {}

    def add_vertex(self, label):
        ''' adds a vertex. label must be a string '''
        if not isinstance(label, str):
            raise ValueError("label must be a string")
        if label in self._vertices:
            raise ValueError("label is already in graph")
        self._vertices[label] = [] # initially empty list of adjacent vertices
        return self

    def add_edge(self, src, dest, weight):
        ''' adds an edge. src, dest must be strings and already added.
        weight must be a positive number '''
        if not isinstance(src, str):
            raise ValueError("src must be a string")
        if not isinstance(dest, str):
            raise ValueError("dest must be a string")
        if not isinstance(weight, (int, float)):
            raise ValueError("weight must be an integer or float")
        if weight <= 0:
            raise ValueError("weight must be positive")
        if src not in self._vertices:
            raise ValueError("src not yet defined in graph")
        if dest not in self._vertices:
            raise ValueError("dest not yet defined in graph")

        weight = float(weight)  # just in case it was passed in as an integer
        adjacent_vertices = self._vertices[src]
        # is dest already in the list of adjacent vertices, then just update it's weight
        for i in range(len(adjacent_vertices)):
            if adjacent_vertices[i][0] == dest:
                adjacent_vertices[i] = (dest, weight)
                self._vertices[src] = adjacent_vertices
                return self
        adjacent_vertices.append((dest, weight))
        return self

    def get_weight(self, src, dest):
        ''' returns the weight of an edge or math.inf is no path
        if src or dest are not defined vertices, ValueError '''
        if src not in self._vertices:
            raise ValueError("src not a defined vertex")
        if dest not in self._vertices:
            raise ValueError("dest not a defined vertex")
        adjacent_vertices = self._vertices[src]  # this is a list of (label, weight) tuples
        for data in adjacent_vertices:
            if data[0] == dest:
                return data[1]
        return math.inf

    def vertices(self):
        ''' Return a list of vertices sorted in natural order. '''
        return sorted(self._vertices)

    def edges(self):
        ''' Return a list of edges where an edge is a triple (src,dest,weight). '''
        edge_list = []
        for src, neighbors in self._vertices.items():
            for dest, weight in neighbors:
                edge_list.append((src,dest,weight))
        return edge_list

    def __str__(self):
        ''' generates a string version of graph '''
        graph_str = "digraph G {\n"
        labels = self._vertices
        for vertex in labels:
            for dest, weight in self._vertices[vertex]:
                graph_str += f'   {vertex} -> {dest} [label="{weight}",weight="{weight}"];\n'
        graph_str += "}\n"
        return graph_str

    def dfs(self, src):
        ''' depth-first tgraversal '''

        if src not in self._vertices:
            raise ValueError("src not a defined vertex")
        visited = []
        stack = [src]
        discovered = set()
        while stack != []:
            vertex = stack.pop()
            if vertex not in discovered:
                discovered.add(vertex)
                visited.append(vertex)
                adjacents = self._vertices[vertex]
                for adj in adjacents:
                    stack.append(adj[0])
        return visited

    def bfs(self, src):
        ''' breadth-first traversal '''
        visited = []
        if src not in self._vertices:
            raise ValueError("src not a defined vertex")
        queue = [src]
        discovered = {src,}
        while queue != []:
            vertex = queue.pop(0)   # slow, but it works
            visited.append(vertex)
            adjacents = self._vertices[vertex]
            for adj in adjacents:
                if adj[0] not in discovered:
                    queue.append(adj[0])
                    discovered.add(adj[0])
        return visited

    def vertex_index(self, target, lyst):
        ''' returns the index of target in lyst '''
        for i in range(len(lyst)):
            if lyst[i][0] == target:
                return i
        raise ValueError("v1 not in Lyst")


    def dsp(self, src, dest):
        ''' performs Dijkstra's Shorted Path algorithm '''
        if src not in self._vertices:
            raise ValueError("src not a defined vertex in graph")
        if dest not in self._vertices:
            raise ValueError("dest not a defined vertex in graph")

        distance = {}
        prev_vertex = {}
        unvisited = []
        for vertex in self._vertices:
            distance[vertex] = math.inf
            unvisited.append((vertex, math.inf))
        distance[src] = 0.0
        prev_vertex[src] = None
        unvisited[self.vertex_index(src, unvisited)] = (src, 0)

        while unvisited:
            # remove the tuple with the min distance
            unvisited.sort(reverse=True, key=lambda x: x[1])
            vertex = unvisited.pop()

            if vertex[1] == math.inf:
                break

            for adjacent in self._vertices[vertex[0]]:
                edge_weight = adjacent[1]
                apd = distance[vertex[0]] + edge_weight

                if apd < distance[adjacent[0]]:
                    distance[adjacent[0]] = apd
                    unvisited[self.vertex_index(adjacent[0], unvisited)] = (adjacent[0], apd)
                    prev_vertex[adjacent[0]] = vertex[0]

        path = []
        if distance[dest] != math.inf:
            path = [dest]
            current_vertex = dest
            while prev_vertex[current_vertex] is not None:
                current_vertex = prev_vertex[current_vertex]
                path.append(current_vertex)
        path.reverse()
        return  (distance[dest], path)


    def dsp_all(self, src):
        ''' performs Dijkstra's Shorted Path algorighm '''
        if src not in self._vertices:
            raise ValueError("src not a defined vertex in graph")

        distance = {}
        prev_vertex = {}
        unvisited = []
        for vertex in self._vertices:
            distance[vertex] = math.inf
            unvisited.append((vertex, math.inf))
        distance[src] = 0.0
        prev_vertex[src] = None
        unvisited[self.vertex_index(src, unvisited)] = (src, 0)

        while unvisited:
            # remove the tuple with the min distance
            unvisited.sort(reverse=True, key=lambda x: x[1])
            vertex = unvisited.pop()

            if vertex[1] == math.inf:
                break

            for adjacent in self._vertices[vertex[0]]:
                edge_weight = adjacent[1]
                apd = distance[vertex[0]] + edge_weight

                if apd < distance[adjacent[0]]:
                    distance[adjacent[0]] = apd
                    unvisited[self.vertex_index(adjacent[0], unvisited)] = (adjacent[0], apd)
                    prev_vertex[adjacent[0]] = vertex[0]

        paths = {}
        for vertex in self._vertices:
            path = []
            if distance[vertex] != math.inf:
                path = [vertex]
                current_vertex = vertex
                while prev_vertex[current_vertex] is not None:
                    current_vertex = prev_vertex[current_vertex]
                    path.append(current_vertex)
            path.reverse()
            paths[vertex] = path

        return paths

def main():
    ''' code starts here'''
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")

    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "F", 9)

    graph.add_edge("B", "F", 6)
    graph.add_edge("B", "D", 15)
    graph.add_edge("B", "C", 8)

    graph.add_edge("C", "D", 1)

    graph.add_edge("E", "C", 7)
    graph.add_edge("E", "D", 3)

    graph.add_edge("F", "B", 6)
    graph.add_edge("F", "E", 3)


    print(graph)

    print("starting DFS with vertex A")
    print("".join(graph.dfs("A")))
    print()

    print("starting BFS with vertex A")
    print("".join(graph.bfs("A")))
    print()

    print("starting DSP from vertex A")
    path = graph.dsp("A", "F")
    print("".join(path))
    print("All DSP shortest paths from from vertex A")
    paths = graph.dsp_all("A")
    for path in paths.values():
        print("".join(path))

def test():
    ''' a second test function '''
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 1.0)
    g.add_edge("A", "C", 1.0)

    g.add_edge("B", "D", 1.0)

    g.add_edge("C", "E", 1.0)

    g.add_edge("E", "F", 1.0)
    print(g)

if __name__ == "__main__":
    main()
    test()
