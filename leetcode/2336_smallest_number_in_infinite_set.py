class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [x for x in range(1, 1001)]
        self.set = set(self.heap)

    def popSmallest(self) -> int:
        val = heappop(self.heap)
        self.set.remove(val)
        return val

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heappush(self.heap, num)
            self.set.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
