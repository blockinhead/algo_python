# encoding: utf8
# нужно найти количество пар чисел, разность между которыми равна заданной

def pairs(k, arr):
    # Write your code here
    res = 0
    vals = {}

    for v in arr:
        vals[v+k] = v

    for v in arr:
        if v in vals:  # and vals[v] != v:
            res += 1

    return res


print(pairs(2, [1, 5, 3, 4, 2]))
