from collections import namedtuple


Pos = namedtuple('Pos', ['x', 'y'])

hm = []

with open('input') as f:
    for l in f:
        hm.append([int(x) for x in l.strip()])


h = len(hm)
w = len(hm[0])


def idx(p: Pos):
    res = []
    if p.x - 1 >= 0:
        res.append(Pos(p.x - 1, p.y))
    if p.x + 1 < w:
        res.append(Pos(p.x + 1, p.y))
    if p.y - 1 >= 0:
        res.append(Pos(p.x, p.y - 1))
    if p.y + 1 < h:
        res.append(Pos(p.x, p.y + 1))

    return res


def getp(p: Pos):
    return hm[p.y][p.x]


mins = []
for y in range(h):
    for x in range(w):
        e = hm[y][x]
        neighbours = [getp(n) for n in idx(Pos(x, y))]
        if not len(list(filter(lambda a: a <= e, neighbours))):
            # print(e)
            # s += (e + 1)
            mins.append(Pos(x, y))


basins = {}
for p in mins:
    seen = {p}
    level = hm[p.y][p.x]
    new = set(idx(p))
    while new:
        if level + 1 == 9:
            break
        for np in list(new):
            if hm[np.y][np.x] == level + 1:
                seen.add(np)
                new.update(set(idx(np)))
        level += 1
        new = new - seen
    print(p, len(seen))
    basins[p] = len(seen)

print(dict(sorted(basins.items(), key=lambda item: item[1], reverse=True)))
