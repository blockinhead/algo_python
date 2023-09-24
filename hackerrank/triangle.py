# https://www.hackerrank.com/challenges/triangle-quest-2/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

N = 5

for i in range(1, N + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(f'{i=}')
    print(*(list(range(1, i + 1)) + list(range(i - 1, 0, -1))), sep='')
    # print('123456789'[:i], '87654321'[-(i - 1):], sep='')
    print('123456789'[:i], '123456789'[:i-1][::-1], sep='')
    print(((10 ** i) // 9) ** 2)
