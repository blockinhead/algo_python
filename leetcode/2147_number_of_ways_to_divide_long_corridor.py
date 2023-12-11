class Solution:
    def numberOfWays(self, corridor: str) -> int:
        stools = 0
        plants = []  # сюда буду складывать количество растений между каждой парой стульев
        current_part = 0

        for c in corridor:
            if c == 'S':
                stools += 1
                current_part += 1

                if current_part == 2:
                    plants.append(0)
                    current_part = 0

            else:  # c == 'P'
                if current_part == 0 and stools >= 2:
                    plants[-1] += 1

        print(plants)
        if stools == 2:
            return 1
        if len(plants) < 2 or stools < 4 or stools % 2 == 1:
            return 0

        m = 10**9 + 7
        plants.pop()  # после последней пары стульев перегородку ставить не надо
        res = 1
        for v in plants:
            res *= (v + 1)  # каждые v растений дают в + 1 вариантов поставить стенку
            res %= m

        return res
