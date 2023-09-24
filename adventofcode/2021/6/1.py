from tqdm import tqdm

digits = [0] * 9
with open('input') as f:
    for x in f.readline().strip().split(','):
        digits[int(x)] += 1

print(digits)
for _ in tqdm(range(256)):
    new_fishes = digits[0]
    for i in range(1, 9):
        digits[i-1] = digits[i]
    digits[8] = new_fishes
    digits[6] += new_fishes
    print(digits)



    # print(digits)
print(sum(digits))
