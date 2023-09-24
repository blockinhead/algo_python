# надо найти сумму цифр в числе, повторяя эту операцию, пока не останется одна цифра
# кроме самого числа даётся ещё количество раз, сколько эти число нужно повторить как строку
# фокус в том, что на входе может быть очень длинное число и очень большое количество повторений
# не стоит прям сразу склеивать гигантсткую строку, повторяя число. повторить к-раз каждую цифру получается быстрее
# при этом можно было бы не просто повторить к раз, но и сумму сразу найти

def _superize(n: str) -> int:
    r = sum([int(d) for d in n])
    if r < 10:
        return r
    else:
        return _superize(str(r))


def super_digit_(n: str, k: int) -> int:
    n_ = [0] * k
    for i in range(k):
        n_[i] = _superize(n)
    if k == 1 and n_[0] < 10:
        return n_[0]

    n = ''.join(map(str, n_))

    return _superize(n)


def super_digit(n: str, k: int) -> int:
    if k == 1:
        return _superize(n)

    n = ''.join([str(int(i) * k) for i in n])
    return _superize(n)


print(super_digit('9875', 4))
