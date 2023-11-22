class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i, l in enumerate(nums):
            for j, v in enumerate(l):
                d[i + j].append(v)

        return [x for v in d.values() for x in v[::-1]]

# диагональ - x + y = const, где const - номер диагонали. таким образом диагонали в словарь попадают в правильнм порядке, дополнительно сортировать не надо
# но строки мы при этом обходим сверху вниз, значит значения в диагонали попадают неправильно, их надо перевернуть
