class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        not_visited = set(range(len(rooms)))

        d = deque([0, ])

        while d:
            next_door = d.pop()
            # print(f'{next_door=}')
            # print(f'{not_visited=}')
            not_visited.discard(next_door)

            for door in rooms[next_door]:
                # print(f'{door=}')
                if door in not_visited:
                    d.append(door)

            # print(f'{d=}')

        # print(f'{not_visited=}')

        return not bool(not_visited)
