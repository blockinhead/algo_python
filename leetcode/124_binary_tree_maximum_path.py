from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val  # float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.res = max(self.res, left if node.left else self.res, right if node.right else self.res)

            left = max(0, left)
            right = max(0, right)

            self.res = max(self.res, node.val, left + node.val + right)

            return node.val + max(left, right)

        dfs(root)
        return self.res


# максимальный вклад в сумму для каждой ноды может быть только значение ноды + максимальная суммы по пути слева или справа (31 строка)
# если путь по ветке даёт отрицательную сумму, то мы просто не будем учитывать такую ветку, нам же не обязательно до листьев доходить (стр 26 27)
# 24 строка обновляет макимальную сумму по веткам (путь максимальной суммы не обязан начинаться в текущей ветке)
# 29 строеп обновляет максимальную сумму если путь максимальной суммы проходит через текущую ноду
