class Node:
    def __init__(self, val=0, node=None):
        self.val = val
        self.next = node

    def __repr__(self):
        return f'<N {self.val}>'


def reverseList(head):
    if not head or not head.next:
        return head

    cur = head
    prev = None

    while cur:
        nxt = cur.next

        cur.next = prev
        prev = cur
        cur = nxt

    return prev


nl = Node(1, Node(2, Node(3, Node(4, None))))
v = reverseList(nl)
print(v)
