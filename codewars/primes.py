def prims(max_n):
    if max_n < 2:
        return [0, 1]

    flags = [True] * (max_n + 1)

    i = 2
    while i < max_n + 1:
        for j in range(2*i, max_n + 1, i):
            flags[j] = False

        i += 1
        while i < max_n and not flags[i]:
            i += 1

    # print(list(enumerate(flags)))

    return [i for i, f in enumerate(flags) if f]


print(prims(500))

