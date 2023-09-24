def maxProfit(prices: list[int]) -> int:
    buy_price = prices[0]
    profit = 0

    for price in prices:
        if price < buy_price:
            buy_price = price
        elif price - buy_price > profit:
            profit = price - buy_price

    return profit


print(maxProfit([7,1,5,3,6,4]))
