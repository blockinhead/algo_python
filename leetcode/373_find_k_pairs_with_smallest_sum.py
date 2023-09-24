from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []

        visited = set((0, 0))
        heappush(heap,
                 (nums1[0] + nums2[0], (0, 0)))  # кладём в хип тупл - (сумма (координата в нумз1, координата в нумз2))

        res = []

        while True:
            if not k or not heap:
                return res

            v, pos = heappop(heap)
            print(f'{v=} {pos=}')
            res.append((nums1[pos[0]], nums2[pos[1]]))

            k -= 1

            # следующая минимальная сумма может быть либо со следующим элементом во втором массиве, либо в первом.
            # чтобы не добавлять в хип то, что там уже есть, используем сет
            if (new_pos := (pos[0], pos[1] + 1)) not in visited and pos[1] + 1 < len(nums2):
                visited.add(new_pos)
                heappush(heap, (nums1[new_pos[0]] + nums2[new_pos[1]], new_pos))

            if (new_pos := (pos[0] + 1, pos[1])) not in visited and pos[0] + 1 < len(nums1):
                visited.add(new_pos)
                heappush(heap, (nums1[new_pos[0]] + nums2[new_pos[1]], new_pos))
