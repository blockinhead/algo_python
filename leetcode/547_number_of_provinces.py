class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        roads = defaultdict(list)
        for i, l in enumerate(isConnected):
            for j, v in enumerate(l):
                if v == 0:
                    continue
                if i == j:
                    continue
                roads[i].append(j)

        visited = [False] * len(isConnected)

        def dive(from_):
            visited[from_] = True
            for next_ in roads[from_]:
                if not visited[next_]:
                    dive(next_)

        provinces = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1
                dive(i)

        return provinces
