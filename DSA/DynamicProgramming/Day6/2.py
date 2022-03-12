"""
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

 

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * 2

        if nums[0] > 0:
            dp[0] = 1
        
        if nums[0] < 0:
            dp[1] = 1
            
        res = dp[0]
        
        for i in range(1, n):
            cur = nums[i]
            tmp = [0] * 2
            if cur > 0:
                tmp[0] = dp[0] + 1
                if dp[1] > 0:
                    tmp[1] = max(tmp[1], dp[1] + 1)
            elif cur < 0:
                tmp[1] = dp[0] + 1
                if dp[1] > 0:
                    tmp[0] = max(tmp[0], dp[1] + 1)
            dp = tmp
            res = max(res, dp[0])
            
        return res