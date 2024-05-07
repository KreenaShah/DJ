from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(int))
        self.nodes = set()

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.nodes.add(u)
        self.nodes.add(v)

    def bfs(self, source, sink, parent):
        visited = {node: False for node in self.nodes}
        queue = [source]
        visited[source] = True
        parent[source] = -1

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    
        return visited[sink]

    def ford_fulkerson(self, source, sink):
        parent = {node: None for node in self.nodes}
        max_flow = 0
        path_count = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            path = []
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                path.insert(0, u)
                v = u
            path.append(sink)
            print(f"Augmenting Path {path_count + 1}: {' -> '.join(path)}")

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            max_flow += path_flow
            path_count += 1

        return max_flow

g = Graph()
g.add_edge("S", "1", 11)
g.add_edge("S", "2", 12)
g.add_edge("2", "1", 1)
g.add_edge("2", "4", 11)
g.add_edge("1", "3", 12)
g.add_edge("4", "3", 7)
g.add_edge("4", "T", 4)
g.add_edge("3", "T", 19)

source = "S"
sink = "T"
print("Max Flow:", g.ford_fulkerson(source, sink))