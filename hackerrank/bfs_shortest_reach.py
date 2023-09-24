from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s, t):
        visited = [False] * (max(self.graph) + 1)
        queue = []

        queue.append(s)
        visited[s] = True
        counter = 0

        while queue:
            s = queue.pop(0)
            counter += 1

            for i in self.graph[s]:
                if i == t:
                    return counter

                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
