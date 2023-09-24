from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        node = head
        while node:
            next = node.next
            node.next = Node(x=node.val, next=next)
            node = next

        node = head
        while node:
            node.next.random = node.random.next if node.random and node.random.next else None
            node = node.next.next

        node = head
        while node:
            print(node.val, node.random.val if node.random else 'null')
            node = node.next

        print('next')

        res = head.next
        res_node = res
        # node = head
        while res_node:
            res_node.next = res_node.next.next if res_node.next and res_node.next.next else None
            # node.next = node.next.next if node.next and node.next.next else None
            print(res_node.val, res_node.random.val if res_node.random else 'null')
            res_node = res_node.next
            # node = node.next

        return res


# сначала встраиваем копии ноды вслед за каждой нодой,
# потом обновляем рандомные указатели,
# потом расплетаем список на на два.
# вернуть оригинальный список в правильное состояние не получилось, но тесты проходит
