def findDuplicate(nums: list[int]) -> int:
    slow = nums[nums[0]]
    fast = nums[nums[nums[0]]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    fast = nums[0]
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]

    return slow

print(findDuplicate([2, 2, 2, 2, 2]))
print(findDuplicate([1, 3, 4, 2, 2]))
