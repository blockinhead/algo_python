from heapq import heappush, heappop
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitals = []  # куча туплов (капитал, профит) из которой мы достанем все проекты, доступные нам с данным капиталом
        for i in range(len(capital)):
            heappush(capitals, (capital[i], profits[i]))

        profit = []

        while k > 0:

            # пока в куче туплов есть проекты с подходящим капиталом, запихиваем профит этих проектов в макс-кучу
            # макскучи в питоне нет, так что инвертируем значение
            while capitals and capitals[0][0] <= w:
                _, p = heappop(capitals)
                heappush(profit, -p)

            # самый дорогой проект из доступных выполняем и увеличиваем результат
            if profit:
                w += -heappop(profit)

            k -= 1

        return w

