import timeit

# https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/train/python


def find_k(n):
    orig_n = n

    res = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            res += 1
        i += 1
    if n > 1:
        print(orig_n, res)
        res += 1

    return res


def count_Kprimes(k, start, end):
    timer_start = timeit.default_timer()
    res = [n for n in range(start, end+1) if find_k(n) == k]
    print('exec time:', timeit.default_timer() - timer_start)
    return res


# print(count_Kprimes(5, 500, 600))
# print(count_Kprimes(1, 1, 20))

# [find_k(n) for n in range(100000)]
find_k(6)
