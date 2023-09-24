from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val} left: {self.left}, right: {self.right}'


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        where_in_inorder = {inorder[i]: i for i in range(len(inorder))}

        # инордер показывает сколько элементов в поддереве. в параметрах функции - какой кусок инордера смотреть
        def _build(root_index, inorder_from, inorder_to):
            # current_subtree_elems = inorder[inorder_from: inorder_to + 1]
            if inorder_from > inorder_to:  # такое бывает в дереве из двух элементов
                return None

            node_val = postorder[root_index]
            node = TreeNode(node_val)

            if inorder_from == inorder_to:  # если поддерево состоит из однго элемента - возвращаем его
                return node

            right_subtree_low = where_in_inorder[node_val] + 1  # всё, что правее рута в инордере - элементы правого поддерева
            next_left_root = postorder[root_index - 1]
            next_right_subtree_elems = inorder[right_subtree_low: inorder_to + 1]
            node.right = _build(root_index - 1, right_subtree_low, inorder_to)  # элемент левее текущего в постордере будет рутом правого поддерева
            num_elems_in_right_subtree = inorder_to - right_subtree_low + 1  # надо посчитать сколько элементов ушло в правое поддерево, потому что рутом левого будет следующий

            left_subtree_high = where_in_inorder[node_val] - 1
            next_right_root = postorder[root_index - num_elems_in_right_subtree - 1]
            next_left_subtree_elems = inorder[inorder_from: left_subtree_high + 1]
            node.left = _build(root_index - num_elems_in_right_subtree - 1, inorder_from, left_subtree_high)

            return node

        return _build(len(inorder) - 1, 0, len(inorder) - 1)




# postorder - [left, right, root]
# inorder - [left, root, right]
# рут - последний элемент постордер
# если посмотреть на этот элемент в инордере, то всё, что левее - левое поддерево. всё что правее - правое.
# следующий с конца элемент постордера - рут правого поддерева. так идём вправо, пока поддерево не будет из одного элемента
# надо посчитать сколько элементов ушло направо, потому что только следующий элемент в постордере будет рутом левого поддерева


print(Solution().buildTree(inorder=[2, 1], postorder=[2, 1]))
print(Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))
