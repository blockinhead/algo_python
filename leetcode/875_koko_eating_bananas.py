class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) >> 1

            eating_time = sum([ceil(p / mid) for p in piles])
            print(f'{mid=} {eating_time=}')

            if eating_time > h:
                low = mid + 1
            else:
                high = mid

        return high
