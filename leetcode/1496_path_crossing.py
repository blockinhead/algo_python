class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x, y = 0, 0
        visited.add((x, y))

        for step in path:
            match step:
                case 'N':
                    y += 1
                case 'S':
                    y -= 1
                case 'E':
                    x += 1
                case 'W':
                    x -= 1
                case _:
                    raise

            # print(f'{x} {y} {visited}')
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))

        return False
