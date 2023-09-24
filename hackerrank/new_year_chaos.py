# encoding: utf8

# люди стояли в очереди. можно было два раза поменяться с впереди стоящим
# выполняется ли это правило для данной очереди? сколько таких перестановок было?
def minimum_bribes(q: list[int]):

    bribes = 0
    index = 0
    while index < len(q) - 1:
        current = q[index]
        if q[index] == index + 1:  # этот человек на месте
            index += 1
            continue

        if abs(index + 1 - q[index]) > 2:  # тут оказался человек, место которого дальше более чем на два
            return 'Too chaotic'

        if q[index] > q[index + 1]:  # если очередь этого человека должна наступить позже чем следующего
            q[index + 1], q[index] = q[index], q[index + 1]  # поменяем их местами
            bribes += 1
            index = max(0, index - 1)  # посмотрим ещё раз на шаг назад
            continue

        print('here?')
        index += 1

    return bribes


print(minimum_bribes([1, 2, 5, 3, 4, 7, 8, 6]))
