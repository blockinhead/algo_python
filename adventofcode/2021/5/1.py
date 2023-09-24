import re


parser = re.compile(r'(?P<x1>[0-9]*),(?P<y1>[0-9]*) -> (?P<x2>[0-9]*),(?P<y2>[0-9]*)')


class Line(object):
    def __init__(self, t: str):
        r = parser.match(t).groupdict()
        self.x1 = int(r['x1'])
        self.y1 = int(r['y1'])
        self.x2 = int(r['x2'])
        self.y2 = int(r['y2'])

    def __repr__(self):
        return '<line %d %d -> %d %d>' % (self.x1, self.y1, self.x2, self.y2)

    @property
    def max(self):
        return max(self.x1, self.x2), max(self.y1, self.y2)


with open('input') as f:
    lines = [Line(l) for l in f]

maxs = [x.max for x in lines]
max_x = max(maxs, key=lambda x: x[0])[0]
max_y = max(maxs, key=lambda x: x[1])[1]

field = []
for _ in range(max_y + 1):
    field.append([0 for x in range(max_x + 1)])

for l in lines:
    if l.y2 < l.y1:
        l.x2, l.x1 = l.x1, l.x2
        l.y1, l.y2 = l.y2, l.y1

    if l.x1 == l.x2:
        for y in range(l.y1, l.y2 + 1):
            field[y][l.x1] += 1

    elif l.y1 == l.y2:
        if l.x1 > l.x2:
            l.x2, l.x1 = l.x1, l.x2
        for x in range(l.x1, l.x2 + 1):
            field[l.y1][x] += 1

    else:
        for n in range(l.y2 - l.y1 + 1):
            if l.x2 > l.x1:
                field[l.y1 + n][l.x1 + n] += 1
            else:
                field[l.y1 + n][l.x1 - n] += 1


accum = 0
for row in field:
    print(*row, sep='')
    for x in row:
        if x > 1:
            accum += 1

print(accum)
