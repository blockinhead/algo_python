# https://leetcode.com/problems/implement-stack-using-queues/
from collections import deque

class MyStack:

    def __init__(self):
        self.d1 = deque()
        self.d2 = deque()

    def push(self, x: int) -> None:
        self.d1.appendleft(x)

    def pop(self) -> int:
        e = self.d1.pop()
        while self.d1:
            self.d2.appendleft(e)
            e = self.d1.pop()
        res = e
        while self.d2:
            self.d1.appendleft(self.d2.pop())
        return res

    def top(self) -> int:
        res = self.pop()
        self.push(res)
        return res

    def empty(self) -> bool:
        return not bool(self.d1)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == '__main__':
    o = MyStack()
    o.push(1)
    o.push(2)
    print(o.top())
    print(o.pop())
    print(o.empty())
