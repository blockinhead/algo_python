# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # print(f'deleting {key=} from {root}')
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        if root.val == key:
            if not root.left and not root.right:
                # print('returning none')
                return None
            if not root.left:
                # print(f'no left, returining right {root.right}')
                return root.right
            if not root.right:
                # print(f'no right, returning left {root.left}')
                return root.left
            # print(f'changin {root.val} to {root.right.val}')
            next_node = root.right
            while next_node.left:
                next_node = next_node.left
            root.val = next_node.val
            # print(f'current right: {root.right}')

            root.right = self.deleteNode(root.right, next_node.val)
            # print(f'new right: {root.right}')

        # print(f'returning final {root}')
        return root