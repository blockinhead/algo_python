import timeit


class FindPrimes(object):
    max_n = 0
    _primes = []

    def __call__(self, max_n):
        # print(self.max_n, len(self._primes))
        if max_n <= FindPrimes.max_n:
            return FindPrimes._primes

        FindPrimes.max_n = max_n
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

        FindPrimes._primes = [i for i, f in enumerate(flags) if f][2:]
        # print('exec time:', timeit.default_timer() - timer_start)

        return FindPrimes._primes


def count_k(k, i, primes):
    timer_start = timeit.default_timer()



    counter = 0
    # orig_i = i
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
    # if counter == k:
    #     res.append(orig_i)

    # print('exec time:', timeit.default_timer() - timer_start)

    return counter


def find_k(n):

    res = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            res += 1
        i += 1
    if n > 1:
        res += 1

    return res


def count_Kprimes(k, start, nd):
    ts = timeit.default_timer()
    res1 = [i for i in range(start, nd + 1) if count_k(k, i, FindPrimes()(nd + 1)) == k]
    print('exec time 1:', timeit.default_timer() - ts)

    ts = timeit.default_timer()
    res2 = [i for i in range(start, nd + 1) if find_k(i) == k]
    print('exec time 1:', timeit.default_timer() - ts)

    print(len(res1) == len(res2))

count_Kprimes(5, 100000, 1000000)

# print(count_k(543223, primes), find_k(543223))
