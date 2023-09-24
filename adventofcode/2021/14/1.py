from more_itertools import pairwise
from collections import Counter

with open('input') as f:
    src = f.readline().strip()
    f.readline()

    d = {}
    for l in f:
        s, _, t = l.strip().split(' ')
        d[s] = t

print(src)
print(d)

'''
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
'''

for i in range(40):
    new_src = [' '] * (len(src) * 2 - 1)
    for j in range(len(src) - 1):
        np = d['%s%s' % (src[j], src[j + 1])]
        # new_src = '%s%s' % (new_src, np)
        new_src[j * 2] = src[j]
        new_src[j * 2 + 1] = np
    new_src[-1] = src[-1]
    # new_src.append('')
    # print(list(zip(new_src, src)))
    # new_src = '%s ' % new_src
    # src = ''.join([x[0]+x[1] for x in zip(new_src, src)]).strip()
    src = new_src
    # print(''.join(new_src))
    print(i)

cou = Counter(src)
print(cou)
print(max(cou.items(), key=lambda x: x[1])[1] - min(cou.items(), key=lambda x: x[1])[1])
