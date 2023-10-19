from collections import deque
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        num = len(leftChild)

        node_parent = [-1] * num
        for i in range(num):
            if (l := leftChild[i]) != -1:
                if node_parent[l] != -1:
                    return False  # more than one parent
                node_parent[l] = i
            if (r := rightChild[i]) != -1:
                if node_parent[r] != -1:
                    return False
                node_parent[r] = i

                # print(f'{node_parent=}')

        root = -1
        for i in range(num):
            if node_parent[i] == -1:
                if root != -1:
                    return False  # more than one root
                root = i

        # print(f'{root=}')

        d = deque()
        d.append(root)
        seen = [False] * num
        while d:
            node = d.pop()
            if seen[node]:
                return False  # cycle
            seen[node] = True

            if (l := leftChild[node]) != -1:
                d.append(l)
            if (r := rightChild[node]) != -1:
                d.append(r)

        # print(f'{seen=} {all(seen)=}')

        return all(seen)
