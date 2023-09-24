from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val} left: {self.left}, right: {self.right}'


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        where_in_inorder = {inorder[i]: i for i in range(len(inorder))}

        root = preorder.pop(0)
        left = self.buildTree(preorder, inorder[: where_in_inorder[root]])
        right = self.buildTree(preorder, inorder[where_in_inorder[root] + 1:])

        return TreeNode(root, left, right)


# preorder - [root, left, right]
# inorder - [left, root, right]
# рут - первый элемент преордер, дальше в нюм левое поддерево, дальше правое
# если найти в инордер рут, то слева там будут элементы левого поддерева, с права - правого
# выкидываем рут из преордера и начинаем строить левое поддерево.
# если в инордере кончились элементы, значит левое поддерево закончилось и можно строить правое.
# к тому моменту из преордера выпадут все элементы, которые были слева,
# так что следующий нулевой элемент преордера - будет рут правого поддерева

print(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
