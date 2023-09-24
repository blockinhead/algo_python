from typing import List

res = []

def subsets(self, nums: List[int]) -> List[List[int]]:
    ans = []

    def dfs(s: int, path: List[int]) -> None:
        print(f'{s=} {path=}')
        ans.append(path)

        for i in range(s, len(nums)):
            index = i + 1
            current_path = path + [nums[i]]
            # dfs(i + 1, path + [nums[i]])
            dfs(index, current_path)

    dfs(0, [])
    return ans

# ans = []
# i = 0..=2:
#    dfs (1, [] + [a])
#       ans = [], [a]
#       i = 1..=2
#       dfs(2, [a] + [b])
#       dfs(3, [a] + [c])
#    dfs (2, [] + [b])
#    dfs (3, [] + [c])

print(subsets(None, [1, 2, 3]))