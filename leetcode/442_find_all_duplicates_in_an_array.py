def findDuplicates(nums: list[int]) -> list[int]:
    res = []
    for i in nums:
        if nums[abs(i) - 1] < 0:
            res.append(abs(i))
        else:
            nums[abs(i) - 1] *= -1
    return res


print(findDuplicates([4,3,2,7,8,2,3,1]))
