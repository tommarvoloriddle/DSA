"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        a = prices
        maxProfit = 0
        currProfit = 0
        i = 1
        if n == 1:
            return 0
        currShare = a[0]
        maxUntilNow = a[0]
        while i < n:
            # print(currShare, currProfit, maxProfit, a[i])
            if a[i] > currShare:
                currProfit = currProfit + (a[i] - currShare)
                currShare = a[i]
                i += 1
            else:
                if currProfit >= 0:
                    maxProfit += currProfit
                currProfit = 0
                currShare = a[i]
                # maxUntilNow = a[i]
                i += 1
        if currProfit >= 0:
            maxProfit += currProfit
        return maxProfit

            # i = 1
#         n = len(prices)
#         currProfit = 0
#         buyPrice = prices[0]
#         totalProfit = 0
#         while i < n:
#             if prices[i] > buyPrice:
#                 profit = abs(prices[i] - buyPrice)
#                 if profit > currProfit:
#                     currProfit = profit
#                 else:
#                     totalProfit += currProfit
#                     currProfit = 0
#                     buyPrice = prices[i]
#             else:
#                 totalProfit += currProfit
#                 buyPrice = prices[i]
#                 currProfit = 0
#             i = i + 1
#         if currProfit >= 0:
#             totalProfit += currProfit

#         return totalProfit
