def caesarChifer(s, k):
    alephbet = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    chifered = {alephbet[i]: alephbet[(i + k) % len(alephbet)] for i in range(len(alephbet))}

    res = []
    for symbol in s:
        if symbol.lower() not in chifered:
            res.append(symbol)
            continue

        new_symbol = chifered[symbol.lower()]
        if symbol.isupper():
            new_symbol = new_symbol.upper()

        res.append(new_symbol)

    return ''.join(res)


print(caesarChifer('middle-Outz', 2))