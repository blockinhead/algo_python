# https://leetcode.com/problems/path-with-minimum-effort/
from pprint import pprint
from collections import namedtuple
import heapq

Pos = namedtuple('Pos', ['x', 'y'])
Step = namedtuple('Step', ['effort', 'pos'])


# heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
# heights = [[1, 10, 6, 7, 9, 10, 4, 9]]
rows = len(heights)
cols = len(heights[0])


def neighbours(pos: Pos) -> list[Pos]:
    res = []
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= pos.x + x < cols and 0 <= pos.y + y < rows:
            res.append(Pos(pos.x + x, pos.y + y))
    return res


visited = set()
steps = [Step(0, Pos(0, 0))]
heapq.heapify(steps)
max_effort = 0

while True:
    print(f'{visited=}\n{steps=}')
    step = heapq.heappop(steps)  # make a step with minimum effort
    visited.add(step.pos)

    max_effort = max(max_effort, step.effort)  # current step may take less effort than prev some prev steps on the way

    if step.pos == Pos(cols - 1, rows - 1):
        print(max_effort)
        break

    nei = neighbours(step.pos)
    for n in filter(lambda x: x not in visited, neighbours(step.pos)):
        heapq.heappush(
            steps,
            Step(effort=abs(heights[n.y][n.x] - heights[step.pos.y][step.pos.x]),  # effrots can be placed in a separate list
                 pos=n)
        )
