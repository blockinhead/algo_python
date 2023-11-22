class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sort_key(n):
            return bin(n).count('1'), n

        return sorted(arr, key=sort_key)
