class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        @cache
        def mp(day, in_stock, profit):
            if day == len(prices):
                return profit

            pr = mp(day + 1, in_stock, profit)  # могу ничего не делать и перейти в следующий день
            if in_stock:
                pr = max(pr, mp(day + 1, False, profit + prices[day]))  # могу продать, перейти в следующий день с профитом от продажи и возможностью купить
            else:
                pr = max(pr, mp(day + 1, True, profit - prices[day] - fee))  # могу купить, заплатив фи и перейти в следующий день, получая возможность продать

            return pr

        return mp(0, False, 0)
        '''

        @cache
        def has_no_stock(day):
            if day == len(prices):
                return 0

            return max(has_stock(day + 1) - prices[day] - fee,  # могу купит, заплатив фи, тогда смогу продать
                       has_no_stock(day + 1))  # могу ничего не делать, перейти в следующий день

        @cache
        def has_stock(day):
            if day == len(prices):
                return 0

            return max(has_stock(day + 1),  # могу не продавая перейти в следующий день
                       has_no_stock(day + 1) + prices[
                           day])  # могу продать, получить прибыль, получу возможность снова покупать

        return has_no_stock(0)
