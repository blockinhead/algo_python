from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d = deque()
        d.append((root, []))

        paths = []

        while d:
            node, path = d.pop()
            if node in (p, q):
                paths.append(path + [node])  # пусть путь включает саму найденную ноду. ведь п, например, может быть этой нодой, а ку - её потомком
                if len(paths) == 2:
                    break
            if node.left:
                d.append((node.left, path + [node]))
            if node.right:
                d.append((node.right, path + [node]))

        # for p in paths[0]:
        #     print(p.val, end=' ')
        # print()
        # for p in paths[1]:
        #     print(p.val, end=' ')
        # print()

        if min(len(paths[0]), len(paths[1])) == 1:
            return root

        # ищем то место, где маршруты расходятся. это и есть ответ
        for i in range(min(len(paths[0]), len(paths[1])) - 1):
            if paths[0][i + 1] != paths[1][i + 1]:
                return paths[0][i]
        # если место не нашлойсь, значит длинный маршрут явлется продолжением короткого. как раз тот случай, что ку потомок п (или наоборот)
        return paths[0][i + 1]

