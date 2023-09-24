class LRUCache:

    def __init__(self, capacity: int):
        self._dict = {}   # в словаре по ключу лежат ноды двусвязанного списка
        self._max_capacity = capacity

        self._head = Node(-1, -1)
        self._tail = Node(-1, -1)
        self._double_link(self._head, self._tail)

    def _add_node(self, node):
        # добавляет ноду в голову
        old_top = self._head.next
        self._double_link(self._head, node)
        self._double_link(node, old_top)
        return node

    def _remove_node(self, node):
        # удаляет ноду
        self._double_link(node.prev, node.next)

    def _double_link(self, node1, node2):
        node1.next = node2
        node2.prev = node1

    def get(self, key: int) -> int:
        if key not in self._dict:
            return -1

        # поднимаем ноду к голове и возвращаем значение
        node = self._dict[key]
        self._remove_node(node)
        self._add_node(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            # обновляем значение
            self.get(key)  # это вытянет ноду наверх
            self._head.next.val = value
            return

        # длинна словаря соответствует длинне списка. если кеш забит, то удаляем ноду из хвоста
        if len(self._dict) == self._max_capacity:
            bottom = self._tail.prev
            self._remove_node(bottom)
            del self._dict[bottom.key]

        # засовываем в словарь свежесозданную ноду
        self._dict[key] = self._add_node(Node(key, value))


class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
