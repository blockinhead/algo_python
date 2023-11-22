class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def neighbours(pos):
            return [(pos[0] - 1, pos[1]),
                    (pos[0] + 1, pos[1]),
                    (pos[0], pos[1] - 1),
                    (pos[0], pos[1] + 1)]

        rotten = deque()
        fresh = set()
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 2:
                    rotten.append((i, j))
                if v == 1:
                    fresh.add((i, j))
        if not fresh:
            return 0

        days = -1
        seen = set()
        while rotten:
            d_ = deque()
            while rotten:
                o = rotten.pop()
                seen.add(o)
                for n in neighbours(o):
                    if n in fresh:
                        d_.append(n)
                        fresh.remove(n)
            rotten = d_
            days += 1

        if fresh:
            return -1

        return days
