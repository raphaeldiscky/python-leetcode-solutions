from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            The key idea is to take down all daily returns and sum up all positive returns.
            This works because we can break every trade down to several overnigt trades.
            For example, considering [1, 2, 3], buy 1 sell 3 is equivalent to buy 1 sell 2 + buy 2 sell 3.
        '''
        if len(prices) == 1:
            return 0

        profit = []

        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1]))
            print("profit", profit)
        return sum(profit)


ob1 = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(ob1.maxProfit(prices))
