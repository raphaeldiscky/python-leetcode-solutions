from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Time: O(n)
        '''
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit


ob1 = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(ob1.maxProfit(prices))
