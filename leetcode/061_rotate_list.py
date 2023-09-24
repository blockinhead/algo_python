from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        length = 1
        n = head
        while n.next:
            length += 1
            n = n.next

        k = k % length

        if k == 0:
            return head

        first = head  # будет смотреть на к-тый с конца элемент - место разреза
        second = head  # будет смотреть на последний элемент

        for _ in range(k):
            first = first.next

        while first.next:
            first = first.next
            second = second.next

        # print(f'{first=}')
        # print(f'{second=}')

        res = second.next  # ответ начинается с хвостика
        second.next = None  # новый хвост должен начинаться с головы и заканчиваться на second, то некст секонда должен быть нан
        first.next = head  # фирст смотрит на последний элемент старого списка, туда мы приклеиваем новый хвост

        return res
