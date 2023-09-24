from collections import namedtuple
from pprint import pprint

Pos = namedtuple('Pos', ['x', 'y'])

hm = []

with open('input') as f:
    for l in f:
        hm.append([int(x) for x in l.strip()])


h = len(hm)
w = len(hm[0])


def idx(p: Pos):
    res = []
    for i in (-1, 0, 1):
        for j in (-1 , 0, 1):
            np = Pos(p.x + i, p.y + j)
            if 0 <= np.x < w and 0 <= np.y < h:
                res.append(np)

    return res


def getp(p: Pos):
    return hm[p.y][p.x]


def incp(p: Pos):
    hm[p.y][p.x] += 1


def flash(p: Pos):
    counter = 1
    hm[p.y][p.x] = 0
    for np in idx(p):
        if getp(np) > 0:
            incp(np)
        if getp(np) == 10:
            counter += flash(np)
    return counter


def step():
    for row in hm:
        for i in range(len(row)):
            row[i] += 1

    c = 0
    to_flash = set()
    for j in range(len(hm)):
        for i in range(len(hm[j])):
            if getp(Pos(i, j)) >= 10:
                c += flash(Pos(i,j))


    pprint(hm)
    print(c)
    return c


def check_zero():
    for row in hm:
        for i in range(len(row)):
            if row[i]:
                return False
    return True


# cou = 0
# for i in range(100):
#     cou += step()
#
# print(cou)

cou = 0
while not check_zero():
    step()
    cou += 1
print(cou)

