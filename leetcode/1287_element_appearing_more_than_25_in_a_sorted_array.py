class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr)
        if l == 1:
            return arr[0]

        q = l // 4
        for i in range(l - q):
            if arr[i] == arr[i + q]:
                return arr[i]

        return -1
