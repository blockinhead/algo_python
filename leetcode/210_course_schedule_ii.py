from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(set)
        for c, p in prerequisites:
            prereqs[c].add(p)

        res = []
        taken = set()

        # seen - для поиска циклов
        # taken - для тех курсов, которые уже прошли. он дублирует рез, но по нему быстрее проверять принадлежность
        def dive(course, seen):
            if course in taken:
                return True
            if course in seen:
                return False

            seen.add(course)
            for p in prereqs[course]:  # проходим по всем зависимостям курса (если они есть)
                if not dive(p, seen):
                    return False

            # если мы тут, то либо у курса нет зависимостей, либо мы уже все видели все зависимости.
            # значит этот курс можно класть в ответ
            res.append(course)
            taken.add(course)

            return True

        for i in range(numCourses):
            if not dive(i, set()):
                return []

        return res


print(Solution().findOrder(numCourses=2, prerequisites=[[0, 1]]))
print(Solution().findOrder(numCourses=2, prerequisites=[[0, 1], [1, 0]]))
print(Solution().findOrder(numCourses=3, prerequisites=[[0, 1], [0, 2], [1, 2]]))
