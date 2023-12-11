class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = defaultdict(int)  # количестов сумм
        d[0] = 1  # 0 - это сумма пустого подмассива, он такой один - nums[0:0]
        current_sum = 0

        for n in nums:
            current_sum += n
            res += d.get(current_sum - k, 0)
            d[current_sum] += 1

        return res

# текущая сумма - sum(nums[0:i]).
# если она на k больше, чем сумма, что мы уже встречали, то nums[j:i] даёт как раз k
