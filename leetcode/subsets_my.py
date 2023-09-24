
def dive(i, accum, nums, res):
    for j in range(i, len(nums)):
        new_accum = accum + [nums[j]]
        res.append(new_accum)
        dive(j + 1, new_accum, nums, res)

def subsets(nums: list[int]) -> list[list[int]]:
    res = [[]]
    dive(0, [], nums, res)
    return res


# print(subsets([1, 2, 3]))
# print(subsets([0]))
print(subsets([1, 2, 2]))