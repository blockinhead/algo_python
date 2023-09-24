def hamming(n):
    hammings = [1] * n
    x2, x3, x5 = 2, 3, 5
    i = j = k = 0

    for n in range(1, n):
        hammings[n] = min(x2, x3, x5)
        print(f'{hammings[n]=} {x2=} {x3=} {x5=} {i=} {j=} {k=}')
        if x2 == hammings[n]:
            i += 1
            x2 = 2 * hammings[i]
        if x3 == hammings[n]:
            j += 1
            x3 = 3 * hammings[j]
        if x5 == hammings[n]:
            k += 1
            x5 = 5 * hammings[k]

    return hammings


print(hamming(30))
