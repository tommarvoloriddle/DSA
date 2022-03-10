"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxUntilNow = [-1]*(len(nums) + 1)
        n = len(nums)
        nums.append(0)
        maxUntilNow[0] = nums[0]
        if nums[1]:
            maxUntilNow[1] = max(nums[0], nums[1])
        x = 0

        def helper(n):
            if maxUntilNow[n] != -1:
                return maxUntilNow[n]
            else:
                if maxUntilNow[n-1] == -1:
                    maxUntilNow[n-1] = helper(n-1)
                if n-2 < 0:
                    maxUntilNow[n] = maxUntilNow[n-1]
                    return maxUntilNow[n-1]
                if maxUntilNow[n-2] == -1:
                    maxUntilNow[n-2] = helper(n-2)
                maxUntilNow[n] = max(maxUntilNow[n-1], maxUntilNow[n-2]+nums[n])
                return maxUntilNow[n]
        helper(n)
        return maxUntilNow[n]
