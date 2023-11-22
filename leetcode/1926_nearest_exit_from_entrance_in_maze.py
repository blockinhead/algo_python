class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        columns = len(maze[0])
        visited = [[False] * columns for _ in range(rows)]
        d = deque([entrance, ])
        visited[entrance[0]][entrance[1]] = True

        def possible_steps(coords):
            res = []
            if 0 <= coords[0] - 1 < rows and maze[coords[0] - 1][coords[1]] == '.':
                res.append((coords[0] - 1, coords[1]))
            if 0 <= coords[0] + 1 < rows and maze[coords[0] + 1][coords[1]] == '.':
                res.append((coords[0] + 1, coords[1]))
            if 0 <= coords[1] - 1 < columns and maze[coords[0]][coords[1] - 1] == '.':
                res.append((coords[0], coords[1] - 1))
            if 0 <= coords[1] + 1 < columns and maze[coords[0]][coords[1] + 1] == '.':
                res.append((coords[0], coords[1] + 1))

            return res

        res = 1
        while d:

            d_ = deque()

            while d:
                step = d.pop()
                for next_ in possible_steps(step):
                    if not visited[next_[0]][next_[1]]:
                        if next_[0] == 0 or next_[1] == 0 or next_[0] == rows - 1 or next_[1] == columns - 1:
                            return res
                        visited[next_[0]][next_[1]] = True
                        d_.append(next_)
            res += 1
            d = d_

        return -1

