
def hamming2():
    h = 1
    _h = [h]    # memoized
    multipliers = (2, 3, 5)
    multindeces = [0 for i in multipliers] # index into _h for multipliers
    multvalues = [x * _h[i] for x, i in zip(multipliers, multindeces)]
    yield h
    while True:
        h = min(multvalues)
        _h.append(h)
        for (n, (v,x,i)) in enumerate(zip(multvalues, multipliers, multindeces)):
            if v == h:
                i += 1
                multindeces[n] = i
                multvalues[n]  = x * _h[i]
        # cap the memoization
        mini = min(multindeces)
        if mini >= 1000:
            del _h[:mini]
            multindeces = [i - mini for i in multindeces]
        #
        yield h


r = 20
for x in hamming2():
    print(x)
    r -= 1
    if not r:
        break
