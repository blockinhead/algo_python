def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev = 1
    current = 2
    for i in range(3, n + 1):
        current, prev = prev + current, current

    return current

print(climbStairs(9))  # 55

