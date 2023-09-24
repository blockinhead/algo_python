from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    maximum = 0

    longest = {n: -1 for n in nums}
    for i in range(len(nums)):
        maximum = max(maximum, search(nums[i], longest))

    return maximum

def search(n, longest):
    if n not in longest:
        return 0

    if (v := longest[n]) != -1:
        return v

    current_longest = 1 + search(n + 1, longest)
    longest[n] = current_longest

    return current_longest


print(longestConsecutive(None, [100,4,200,1,3,2]) == 4)
