open_braces = ('(', '[', '{', '<')
close_braces = (')', ']', '}', '>')
vals = {')': 3, ']': 57, '}': 1197, '>': 25137}
vals2 = {'(': 1, '[': 2, '{': 3, '<': 4}

s = 0
s_ac = []
with open('input') as f:
    for l in f:
        cache = []
        for c in l.strip():
            # print(c)
            if c in open_braces:
                cache.append(open_braces.index(c))
            else:
                if cache[-1] == close_braces.index(c):
                    cache.pop()
                else:
                    s += vals[c]
                    cache = []
                    break

        if cache:
            s2 = 0
            # print(cache)
            print(*[open_braces[i] for i in cache], sep='', end=' ')
            while cache:
                c = cache.pop()
                s2 = s2 * 5 + vals2[open_braces[c]]
            print(s2)
            s_ac.append(s2)


print(s)
print(sorted(s_ac)[(len(s_ac) - 1) // 2])
