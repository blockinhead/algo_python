from more_itertools import pairwise


with open('input.txt') as f:
    digits = [int(line) for line in f]


counter = 0
for x, y in pairwise(digits):
    if y - x > 0:
        counter += 1

print(counter)

