from typing import List


'''
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    presence_flags = [False] * (len(nums) + 1)
    for i in nums:
        presence_flags[i] = True

    print(presence_flags)
    print(presence_flags[1:])

    return [i for i, f in enumerate(presence_flags[1:], 1) if not f]
'''


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    for i in nums:
        nums[abs(i) - 1] = - abs(nums[abs(i) - 1])
    return [i for i, f in enumerate(nums, 1) if f > 0]

print(findDisappearedNumbers([2, 2, 2]))
