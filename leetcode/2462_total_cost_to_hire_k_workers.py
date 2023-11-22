class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = costs[:candidates]
        right_heap = costs[max(candidates, len(costs) - candidates):]  # справа либо по количеству кандидатов, либо всё что осталось после левого хипа
        # print(f'{max(candidates, len(costs) - candidates)=} {len(left_heap)=} {len(right_heap)=}')
        heapify(left_heap)
        heapify(right_heap)
        # print(f'{left_heap=} {right_heap=}')


        left = candidates  # следующий элемент слева
        right = len(costs) - candidates - 1  # следующий элемент справа

        res = 0

        for _ in range(k):
            # print(f'{left_heap=} {right_heap=}')
            # так как к <= длинны массива, то либо левая, либо правая кучи наверняка есть
            # если минимальные значения одинаковые, берём из левой кучи
            if (not right_heap) or (left_heap and left_heap[0] <= right_heap[0]):
                # print('pop left')
                res += heappop(left_heap)
                # так как лефт и райт - это не текущий, а следующий элемент, то смотрим не просто <, а <=
                if left <= right:
                    heappush(left_heap, costs[left])
                    left += 1
            else:
                # print('pop right')
                res += heappop(right_heap)
                if left <= right:
                    heappush(right_heap, costs[right])
                    right -= 1

        return res



