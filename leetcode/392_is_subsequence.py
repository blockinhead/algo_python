def isSubsequence(s: str, t: str) -> bool:
    si = 0
    ti = 0

    while ti < len(t) and si < len(s):
        ss = s[si]
        tt = t[ti]

        if s[si] != t[ti]:
            ti += 1
            continue
        else:
            si += 1
            ti += 1

        # if ti == len(t) - 1 and si != len(s) - 1:
        #     return False

    return ti == len(t) and si == len(s)

print(isSubsequence('abc', "ahbgdc"))
print(isSubsequence('axc', "ahbgdc"))
