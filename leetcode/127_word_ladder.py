from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def can_mutate(a, b):
            ok = False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if not ok:
                        ok = True
                    else:
                        return False
            return ok

        mutations = deque()
        mutations.append((beginWord, 0))

        seen = set(beginWord)

        # точно то же, что и 433, но для кратчайшего пути нужно искать в ширину, а не в глубину.
        # для поиска в ширину нужно перебрать все варианты на текущем уровне, а потом переходить на следующий. отсюда два вайла
        while mutations:

            next_mutations = deque()
            while mutations:
                mutation, num_step = mutations.pop()
                for g in wordList:
                    if can_mutate(mutation, g) and g not in seen:
                        # print(f'{g=} {num_step=}')
                        if g == endWord:
                            return num_step + 2

                        seen.add(g)
                        next_mutations.append((g, num_step + 1))
            mutations = next_mutations

        return 0
