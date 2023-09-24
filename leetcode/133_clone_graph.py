from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        q = deque()
        clones = dict()

        def get_or_add_clone(some_node):
            already_seen = True
            if some_node.val not in clones:
                already_seen = False
                clones[some_node.val] = Node(some_node.val, [])
            return clones[some_node.val], already_seen

        q.append(node)
        get_or_add_clone(node)

        while q:
            current_node = q.pop()
            clone, _ = get_or_add_clone(current_node)

            for n in current_node.neighbors:
                n_clone, already_seen = get_or_add_clone(n)
                if not already_seen:
                    q.append(n)
                clone.neighbors.append(n_clone)

        # for k in clones:
            # print(clones[k].val, len(clones[k].neighbors))

        return clones[node.val]
    