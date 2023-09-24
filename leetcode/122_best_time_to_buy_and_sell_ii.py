def maxProfit(prices: list[int]) -> int:
    # https://github.com/brianchiang-tw/leetcode/tree/master/No_0122_Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II

    prev_hold = -float('inf')  # сколько у меня денег, если я держу акции (на первом шаге такого быть не может)
    prev_not_hold = 0          # сколько у меня денег, если я не держу акции

    for price in prices:
        hold = max(prev_hold, prev_not_hold - price)      # либо я продолжаю держать, либо у меня не было акций и я покупаю по цене прайс
        not_hold = max(prev_not_hold, prev_hold + price)  # либо у меня ничего не куплено, есть кеш, либо я продаю акции, которые купил раньше по цене прайс

        prev_not_hold = not_hold
        prev_hold = hold

    return not_hold  # у меня справшивают макс профит, то есть акций у меня быть не должно



def _maxProfit(prices: list[int]) -> int:
    '''
    так как ограничений на количество сделок нет, можно покупать каждый раз, когда цена увеличивалась,
    те если цена в текущий день больше чем в предыдущий, надо покупать
    '''
    profit = 0
    for i in range(1, len(prices)):
        profit += max(0, prices[i] - prices[i - 1])

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))
