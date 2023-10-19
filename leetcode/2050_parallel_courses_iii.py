from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        num_prereq = [0] * (n + 1)  # сколько курсов нужно пройти перед теме пройти данный
        # кукрсы нумеруются с единицы, чтоб не гонять индекс вниз всё время, добавлю незначащий ноль в начале
        for pre, cou in relations:
            graph[pre].append(cou)  # какие курсы можно будет пройти после данного
            num_prereq[cou] += 1

        d = deque()  # кладу в декуте курсы, у которых нет пререквестов
        for i in range(1, n + 1):
            if not num_prereq[i]:
                d.append(i)

        times = [0] + time  # сколько требуется времени чтобы пройти данный курс влючая пререквесты. тут тоже незначащий ноль в начале

        while d:
            course = d.pop()
            for next_course in graph[course]:
                # на то чтобы пройти следующий курс потребуется время прохождения текущего курса + время прохождения следующего (-1 в индексе, потому что там индекс не сдвинут)
                # возможно, у другого курса times[course] было больше
                times[next_course] = max(times[next_course], times[course] + time[next_course - 1])
                num_prereq[next_course] -= 1
                if num_prereq[next_course] == 0:
                    # если у этого курсе теперь нет пререквестов, то кладу его в деку, чтобы смотреть в графе какие курсы можно пройти после него
                    d.append(next_course)

        return max(times)
