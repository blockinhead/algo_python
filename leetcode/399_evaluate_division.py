from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dive(a, b, graph, seen):
            if a not in graph:
                return -1.0
            if a == b:
                return 1.0

            seen.add(a)

            # ищем в словаре, есть ли искомое отношение
            for (b_, val) in graph[a]:
                if b_ == b:
                    return val

            # если нет, то посмотрим по другим вершинам, вдруг есть можно найти путь через промежуточную ноду
            for (b_, val) in graph[a]:
                if b_ not in seen:  # чтобы не зациклиться
                    ratio = dive(b_, b, graph, seen)
                    if ratio != -1:
                        graph[a].add((b, ratio * val))  # добавим найденное соотношение, вдруг пригодится
                        return ratio * val

            return -1.0

        graph = defaultdict(set)

        # для всех доступных длинн строи словарь отношений. получается граф
        for (a, b), val in zip(equations, values):
            graph[a].add((b, val))
            graph[b].add((a, 1 / val))

        return [dive(a, b, graph, set()) for a, b in queries]
