"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = prices
        n = len(a)
        # m = [-1]*n
        # maxi = -1
        # for i in range(n-1, -1, -1):
        #     m[i] = maxi
        #     if a[i] > maxi:
        #         maxi = a[i]
        # ans1 = -1
        # for i in range(0, n-1):
        #     ans1 = max(ans1, (m[i] - a[i]))
        # if ans1 <= 0:
        #     ans1 = 0
        # # return ans1
        maxi = -1
        maxUntilNow = a[n-1]
        if n == 1:
            return 0
        for i in range(n-2, -1, -1):
            if a[i] > maxUntilNow:
                maxUntilNow = a[i]
            else:
                if (maxUntilNow - a[i]) > maxi:
                    maxi = maxUntilNow - a[i]
        return max(maxi, 0)
