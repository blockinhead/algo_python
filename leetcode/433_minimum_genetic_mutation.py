class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def can_mutate(a, b):
            ok = False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if not ok:
                        ok = True
                    else:
                        return False
            return ok

        next_mutations = deque()
        next_mutations.append((startGene, 0))

        seen = set(startGene)

        while next_mutations:
            mutation, num_step = next_mutations.pop()

            for g in bank:
                if can_mutate(mutation, g) and g not in seen:
                    # print(f'{g=} {num_step=}')
                    if g == endGene:
                        return num_step + 1

                    seen.add(g)
                    next_mutations.append((g, num_step + 1))

        return -1
