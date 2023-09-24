import statistics

with open('input') as f:
    digits = [int(x) for x in f.readline().strip().split(',')]

# target_pos = round(statistics.mean(digits))
target_pos = sum(digits) // len(digits)
print(f'{target_pos=}')


total_fuel = 0
for d in digits:

    total_fuel += sum(range(abs(d - target_pos) + 1))

print(total_fuel)