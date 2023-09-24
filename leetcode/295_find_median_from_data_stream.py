from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.minheap = []  # здесь будет правая часть текущего состояния (большие числа)
        self.maxheap = []  # здесь будет левая часть (маленькие числа). максхипа в питоне нет, так что надо инвертировать значения
        # мединана будет на стыке двух куч

    def addNum(self, num: int) -> None:
        if self.minheap and self.minheap[0] < num:
            heappush(self.minheap, num)
        else:
            heappush(self.maxheap, -num)

        # если кучи отличаютс друг от другга больше чем на один элемент, то надо их ребалансировать
        if len(self.minheap) == len(self.maxheap) + 2:
            heappush(self.maxheap, -heappop(self.minheap))
        if len(self.maxheap) == len(self.minheap) + 2:
            heappush(self.minheap, -heappop(self.maxheap))

        # print(f'push {num}: {self.minheap=} {self.maxheap=}')

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2

        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]

        return -self.maxheap[0]

    # Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
