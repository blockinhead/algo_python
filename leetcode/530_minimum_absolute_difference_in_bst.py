from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        d = deque()
        current_node = root

        prev_val = None
        min_dif = float('inf')

        while d or current_node:
            if current_node:  # пока можем, идём налево
                d.append(current_node)
                current_node = current_node.left
            else:
                # дальше налево некуда, откатываем стек на один шаг и идём на один шаг направо.
                # если направо тоже некуда, то опять откатываем стек на один шаг.
                # получается, что если узлов всего три, то так мы сначала добавим в стек корень, потом левого,
                # потом откатим левого, потому что левого потомка у него уже нет,
                # потом откатим корень, потому что правого потомка у левого тоже нет. и добавим правого.
                # так получается что инфиксный обход бст даёт отсортированный массив
                node = d.pop()
                print(node.val)

                if prev_val is None:
                    prev_val = node.val
                else:
                    min_dif = min(min_dif,
                                  node.val - prev_val)  # так как массив отсортирован, минимальная разница всеми возможными парами - это минимальная разница между двумя соседними элементами
                    prev_val = node.val

                current_node = node.right

        return min_dif
