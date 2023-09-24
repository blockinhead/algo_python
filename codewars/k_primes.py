import timeit


def find_primes(max_n):
    timer_start = timeit.default_timer()
    # if max_n < 2:
    #     return [0, 1]

    flags = [True] * (max_n + 1)

    i = 2
    while i < max_n + 1:
        for j in range(2*i, max_n + 1, i):
            flags[j] = False

        i += 1
        while i < max_n and not flags[i]:
            i += 1

    # flags.pop(0)
    # flags.pop(0)
    # print(list(enumerate(flags)))

    res = [i for i, f in enumerate(flags) if f]
    print('exec time:', timeit.default_timer() - timer_start)

    return res[2:]


def k_primes(k, a, b, primes=None):
    timer_start = timeit.default_timer()

    if not primes:
        primes = find_primes(b)
    res = []
    # print(primes)

    for i in range(max(2, a), b + 1):

        counter = 0
        orig_i = i
        for j in primes:
            if j * j > i:
                break
            if counter > k:
                break
            while i % j == 0:
                i //= j
                counter += 1
        if i > 1:
            counter += 1
        if counter == k:
            res.append(orig_i)

    print('exec time:', timeit.default_timer() - timer_start)

    return res


def puzzle(s):
    primes = find_primes(s)

    counter = 0
    for c in k_primes(7, 4, s, primes):
        for b in k_primes(3, 3, s - c, primes):
            for a in primes:
                if a > s - c - b:
                    break
                if a + b + c == s:
                    counter += 1
    return counter


print(k_primes(3, 0, 100))
# print(puzzle(143))
