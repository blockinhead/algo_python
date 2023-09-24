with open('input') as f:
    digits = [line for line in f]

accum = [0] * (len(digits[0]) - 1)

for d in digits:
    for i, a in enumerate(d.strip()):
        accum[i] += int(a)


gamma = ''
epsilon = ''

for a in accum:
    if a > len(digits) / 2.0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, base=2) * int(epsilon, base=2))
