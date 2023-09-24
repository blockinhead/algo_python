from more_itertools import windowed, pairwise


with open('input.txt') as f:
    digits = [int(line) for line in f]

composed_digits = map(sum, windowed(digits, 3))

counter = 0
for x, y in pairwise(composed_digits):
    if y - x > 0:
        counter += 1

print(counter)
