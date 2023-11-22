class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def rev(val):
            res = 0
            while val > 0:
                res *= 10
                res += val % 10
                val //= 10
            return res

        d = defaultdict(int)
        res = 0
        for val in nums:
            x = val - rev(val)
            res += d.get(x, 0)
            d[x] += 1

        return res % MOD

#     nums[i] + rev(nums[j]) = nums[j] + rev(nums[i]) =>
# =>  nums[i] - rev(nums[i]) = nums[j] - rev(nums[j])
# считаю для всех чисел nums[i] - rev(nums[i])
# если нахажу число с таким же значением - значит есть пара
# если найду ещё одно с таким же значением, значит пар на две больше...
