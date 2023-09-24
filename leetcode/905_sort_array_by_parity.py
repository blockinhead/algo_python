# https://leetcode.com/problems/sort-array-by-parity/

nums = [3, 1, 2, 4]

res = [0] * len(nums)
odd = 0
even = len(nums) - 1

for n in nums:
    if n % 2:
        res[even] = n
        even -= 1
    else:
        res[odd] = n
        odd += 1

print(res)

