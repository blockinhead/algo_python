class StockSpanner:

    def __init__(self):
        self.d = deque()  # price, days

    def next(self, price: int) -> int:
        prev_days = 1
        while self.d and self.d[-1][0] <= price:
            val, days = self.d.pop()
            prev_days += days

        self.d.append((price, prev_days))

        return prev_days

# всё, что меньше текущей цены нужно выкинуть из стека и записать в стек, сколько там было дней в этих записях


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
