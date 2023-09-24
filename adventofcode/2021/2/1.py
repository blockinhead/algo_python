
horizontal = 0
depth = 0
aim = 0

with open('input.txt') as f:
    for l in f:
        direction, amount = l.split()
        amount = int(amount)
        if direction == 'forward':
            horizontal += amount
            depth += (aim * amount)
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount

print(horizontal * depth)
