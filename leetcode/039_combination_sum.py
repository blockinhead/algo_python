from typing import List


class Solution:
    candidates = []
    res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.res = []
        self.dive([], target, 0)
        return self.res


    def dive(self, accum, current_target, start_index):
        if current_target < 0:
            return

        if current_target == 0:
            self.res.append(accum[:])

        for i in range(start_index, len(self.candidates)):
            # смотрим на числа только начиная с iтого. иначе комбинации будут с перестановками
            # апенд и поп получаются быстрее, чем конкатенация. при конкатенации создаётся новый экземпляр списка
            accum.append(self.candidates[i])
            # self.dive(accum + [self.candidates[i]], current_target - self.candidates[i], i)
            self.dive(accum, current_target - self.candidates[i], i)
            accum.pop()
