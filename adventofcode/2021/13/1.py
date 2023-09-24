from collections import namedtuple
from pprint import pprint

dot = namedtuple('dot', ['x', 'y'])

folds = []
dots = []



with open('input') as f:
    for l in f:
        l = l.strip()
        if l:
            if l.startswith('fold'):
                folds.append(l.split(' ')[-1].split('='))
            else:
                x, y = l.split(',')
                dots.append(dot(int(x), int(y)))
print(dots)
print(folds)

# max_x = max(dots, key=lambda x: x.x).x
# max_y = max(dots, key=lambda x: x.y).y
# print(f'{max_x=} {max_y=}')
#
# f = []
# for _ in range(max_y + 1):
#     f.append(['_' for x in range(max_x + 1)])
# for d in dots:
#     f[d.y][d.x] = '*'
# for r in f:
#     print(*r, sep='')
# print()
#
# exit()

for fold in folds:
    new_dots = set()
    fold_shift = int(fold[1])
    if fold[0] == 'y':
        for d in dots:
            if d.y > fold_shift:
                new_d = dot(d.x, fold_shift - (d.y - fold_shift))
                new_dots.add(new_d)
            else:
                new_dots.add(d)
    else:
        for d in dots:
            if d.x > fold_shift:
                new_d = dot(fold_shift - (d.x - fold_shift), d.y)
                new_dots.add(new_d)
            else:
                new_dots.add(d)

    dots = new_dots


max_x = max(dots, key=lambda x: x.x).x
max_y = max(dots, key=lambda x: x.y).y
print(f'{max_x=} {max_y=}')
f = []
for _ in range(max_y + 1):
    f.append([' ' for x in range(max_x + 1)])
for d in dots:
    f[d.y][d.x] = '*'
for r in f:
    print(*r, sep='')

print(len(new_dots))
