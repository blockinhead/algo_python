class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph_from = defaultdict(list)
        graph_to = defaultdict(list)
        for from_, to_ in connections:
            graph_from[from_].append(to_)
            graph_to[to_].append(from_)

        visited = [False] * n
        res = 0

        # print(f'{graph_to=}')
        # print(f'{graph_from=}')

        def go(city):
            # print(f'{city=} {graph_to[city]=} {graph_from=}')
            visited[city] = True
            for next_ in graph_to[city]:
                if not visited[next_]:
                    # print(f'moving from {city} to {next_}')
                    go(next_)
            for next_ in graph_from[city]:
                if not visited[next_]:
                    # print(f'reversing from {city} to {next_}')
                    nonlocal res
                    res += 1
                    go(next_)

        go(0)

        return res
