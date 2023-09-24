from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        node = root

        while node:
            if node.left:  # если есть нода слева, то мы хотим повесить её направо
                if node.right:  # но если справа место занято
                    # ищем у левой ноды свободное место справа, чтобы перевесить правое поддерево туда,
                    # чтобы освободить место под левую ноду
                    # (в принципе можно повесить на первое попавшееся свобоное место,
                    # но мы же хотим чтобы линкед лист был справа, так что сразу делаем красиво)
                    left_rightmost = node.left
                    while left_rightmost.right != None:
                        left_rightmost = left_rightmost.right
                    left_rightmost.right = node.right  # перевесили
                    node.right = None                  # освободили
                node.right = node.left  # перевесили
                node.left = None        # слева больше ничего нет, кусок линкедлиста готов
            node = node.right           # смотрим дальше
