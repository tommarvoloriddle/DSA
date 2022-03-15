"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        a = prices
        hold = [0]*(n)
        nohold = [0]*(n)

        if n == 1:
            return 0

        if n == 2:
            return max(a[1]-a[0], 0)

        dp_buy          = [0 for _ in range(n)]
        dp_cooldown     = [0 for _ in range(n)]
        dp_sell         = [0 for _ in range(n)]

        dp_cooldown[0]  = 0
        dp_buy[0]       = -prices[0]
        dp_sell[0]      = float('-inf')
        max_prev_buy    = dp_buy[0]

        for i in range(1, n):
            dp_cooldown[i]  = max( dp_cooldown[i-1], dp_buy[i-1], dp_sell[i-1] )
            dp_buy[i]       = dp_cooldown[i-1] - prices[i]
            dp_sell[i]      = max_prev_buy + prices[i]

            max_prev_buy    = max( max_prev_buy, dp_buy[i] )

        return max( dp_cooldown[-1], dp_sell[-1] )
