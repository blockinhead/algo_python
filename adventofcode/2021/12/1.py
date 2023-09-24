from collections import defaultdict
from pprint import pprint


r = defaultdict(list)
small_caves = set()
with open('input') as f:
    for l in f:
        l = l.replace('end', 'End')
        l = l.replace('start', 'Start')
        k, v = l.strip().split('-')

        for _k, _v in [(k, v), (v, k)]:
            if _k != 'End' and _v != 'Start':
                r[_k].append(_v)

        if v.islower():
            small_caves.add(v)
pprint(r)
print(f'{small_caves=}')
# exit()


def check_route(route_, t):
    if t not in route_:
        return True
    for c in small_caves:

        if route_.count(c) >= 2:


            # print(f'flase, {route_=}, {t=}')
            return False
    return True


routes = {('Start',)}

while True:
    new_routes = set()
    for route in routes:
        to_ = r[route[-1]]
        if not to_:
            new_routes.add(route)
        for t in to_:
            if t.islower() and not check_route(route, t):
                continue
            new_route = tuple(list(route) + [t])
            if new_route in routes or new_route in new_routes:
                continue

            new_routes.add(new_route)

    # pprint(new_routes)
    # print()
    if routes == new_routes:
        break

    routes = new_routes

print(len(routes))

# pprint(routes)
