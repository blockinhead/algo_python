class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        current = root

        while current:

            dummy = Node()  # вешаем ноду, по которой мы потом сможем найти начало уровня. начало уровня нужно потому, что его лефт будет началом следующего уровня (или райт, если лефта нет)
            next_layer = dummy  # а через эту переменную будем связывать ноды на следующем уровне

            current_layer = current

            while current_layer:  # идём по всем нодам текущего уровня, они же связаны через некст

                if current_layer.left:
                    next_layer.next = current_layer.left
                    next_layer = next_layer.next
                if current_layer.right:
                    next_layer.next = current_layer.right
                    next_layer = next_layer.next

                current_layer = current_layer.next

            current = dummy.next  # вот первая нода следующего уровня стала новым рутом

        return root


# берём рут. вешаем дами и к нему левого и правого ребёнка. у рута некста нет, так что из внтуреннего цикла вываливаемся
# к дамми был подвешен левый ребёнок рута. он наш новый рут.
# но к нему некстом уже подвешен правый ребёнок рута, так что если оба ребёнка у рута были,
# то на второй итерации из внутреннего цикла мы так быстро как на первом шаге уже не вывалимся
