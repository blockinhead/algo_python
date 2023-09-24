from collections import deque, defaultdict
from heapq import heappop, heappush


class MinStack:

    def __init__(self):
        self.deque = deque()
        self.heap = []
        self.elems = defaultdict(int)

    def push(self, val: int) -> None:
        self.deque.append(val)
        self.elems[val] += 1
        heappush(self.heap, val)

    def pop(self) -> None:
        val = self.deque.pop()
        self.elems[val] -= 1
        v = heappop(self.heap)
        if v != val:
            heappush(self.heap, v)

    def top(self) -> int:
        return self.deque[-1]

    def getMin(self) -> int:
        val = heappop(self.heap)
        while self.elems[val] == 0:
            val = heappop(self.heap)
        heappush(self.heap, val)
        return val


# правильное решение - вместо словаря и минхипа использовать второй стек.
# во второй стек при пуше попадает либо ещё раз верхушка второго стека, либо сам элемент, смотря что меньше.
# поп удаляет элемент из обоих стеков.

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()  # return -3
minStack.pop()
minStack.top()    # return 0
minStack.getMin()  # return -2