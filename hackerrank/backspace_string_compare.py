def backspaceCompare(s: str, t: str) -> bool:
    '''
    ss = []
    tt = []
    for ch in s:
        if ch != '#':
            ss.append(ch)
        elif ss:
            ss.pop()

    for ch in t:
        if ch != '#':
            tt.append(ch)
        elif tt:
            tt.pop()

    return ss ==tt
    '''

    si = len(s) - 1
    ti = len(t) - 1

    while si != -1 or ti != -1:
        if s[si] == '#':
            si = fni(s, si)
        if t[ti] == '#':
            ti = fni(t, ti)
        if si == -1 and ti == -1:
            return True
        if si == -1 or ti == -1:
            return False

        if s[si] == t[ti]:
            si -= 1
            ti -= 1
        else:
            return False

    return True

def fni(s, i):
    skips = 0
    while i>= 0:
        if s[i] == '#':
            skips += 1
            i -= 1
        elif skips > 0:
            skips -= 1
            i -= 1
        else:
            return i

    return i


print(backspaceCompare('ab#c', 'ad#c'))
print(backspaceCompare('ab##', 'c#d#'))
print(backspaceCompare('bxj##tw', 'bxo#j##tw'))
print(backspaceCompare('bxj##t', 'bxj###t'))

