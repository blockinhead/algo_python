class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        h = []
        for n, c in count.items():
            heappush(h, (-c, n))

        return [heappop(h)[1] for _ in range(k)]
