res = []
n = 5
k = 2


def dive(accum: list, start: int):
    if len(accum) == k:
        res.append(accum[:])

    # пуш и поп - это поставить на текущее место все возможные цифры,
    # и поставить на следующие места все возможные цифры, начиная с данной
    # те если на текущее место мы поставили 2, то на следующее можно поставить 3, 4, 5...
    for i in range(start, n + 1):
        accum.append(i)
        dive(accum, i + 1)
        accum.pop()

dive([], 1)

print(res)
