class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        # print(f'{nums=}')

        current_sum = 0  # здесь собираю сумму окна длинны к из н1
        heap = []  # здесь будет минхи того, что я запихнул в сумму, чтобы когда окно сдивгается, выкидывать из него самое маленькое значение
        res = 0

        for n1, n2 in nums:
            current_sum += n1
            heappush(heap, n1)

            if len(heap) < k:  # окно длинны к ещё не набралось
                continue

            if len(heap) > k:  # окно переполнилось - значит надо выкинуть что-то. выкидываю самое маленькое значение, мне же нужно чтобы сумма окна была как можно больше
                current_sum -= heappop(heap)

            if len(heap) == k:  # домножаю макисмально возможную сумму на минимальный элемент из нумз2. это текущий элемент, потому что нумз2 у меня отсортирован по убыванию
                res = max(res, current_sum * n2)

        return res
