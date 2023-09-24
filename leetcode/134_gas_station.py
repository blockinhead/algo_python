from  typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        current_tank = 0
        current_start = 0
        total_tank = 0

        for station, (to_tank, dist) in enumerate(zip(gas, cost)):
            current_tank += (to_tank - dist)
            total_tank += (to_tank - dist)
            if current_tank < 0:
                current_start = station + 1
                current_tank = 0

        if total_tank < 0:
            return -1

        return current_start % len(cost)


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
