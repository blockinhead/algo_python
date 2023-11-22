class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()

        # сентаоры будут голосовать по очереди. одна партия против другой
        for i, m in enumerate(senate):
            if m == 'R':
                r.append(i)
            else:
                d.append(i)

        next_turn = len(senate)
        while r and d:  # пока одна из очередей на проголосовать не обнулится
            # если очередь сенатора из р наступает раньше, чем сенатора из д, то д выбывает из голосования, а р сможет проголосовать ещё раз в следующую очередь
            # и наоборот
            if r.popleft() < d.popleft():
                r.append(next_turn)
            else:
                d.append(next_turn)
            next_turn += 1

        return 'Radiant' if r else 'Dire'
