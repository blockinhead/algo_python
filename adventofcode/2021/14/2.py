from more_itertools import pairwise
from collections import Counter, defaultdict

with open('input') as f:
    src = f.readline().strip()
    f.readline()

    d = {}
    for l in f:
        s, _, t = l.strip().split(' ')
        d[s] = t

print(src)
print(d)
d = {k: [k[0] + v, v + k[1]] for k, v in d.items()}
print(d)
src = {''.join(x): 1 for x in pairwise(src)}
print(src)
# exit()

'''
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
'''

pairs = defaultdict(int)
for a, b in pairwise(src):
    k = a + b
    pairs[k] += 1

print(pairs)

for i in range(10):
    new_src = defaultdict(int)
    for p, c in src.items():
        for d_ in d[p]:
            new_src[d_] += c
    src = new_src

count = defaultdict(int)
for p, c in src.items():
    for ch in p:
        count[ch] += c


print(count)

print(count)
max_k = max(count, key=lambda x: count[x])
min_k = min(count, key=lambda x: count[x])
print(max_k, min_k)
print(count[max_k] // 2 - count[min_k] // 2)
print((max(count.values()) + 1) // 2 - (min(count.values()) + 1) // 2)


