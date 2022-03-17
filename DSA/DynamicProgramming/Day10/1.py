"""
413. Arithmetic Slices
Medium

3768

248

Add to List

Share
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
Accepted
220,516
Submissions
343,121
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0

        currentDiff = nums[1] - nums[0]
        ans = 0
        currAns = 2
        i = 2
        while i < n:
            # print(i, nums[i] , nums[i-1], currentDiff)
            if (nums[i] - nums[i-1]) == currentDiff:
                currAns += 1
                i += 1
            else:
                currentDiff = nums[i] - nums[i-1]
                if currAns >= 3:
                    x = currAns
                    noOfSubs =  (x * (x + 1) )//2
                    noOfSubs = noOfSubs - x - (x - 1)
                    ans = ans + noOfSubs
                # print("change", ans, currentDiff)
                currAns = 2
                i += 1
        if currAns >= 3:
            x = currAns
            noOfSubs =  (x * (x + 1) )//2
            noOfSubs = noOfSubs - x - (x - 1)
            ans = ans + noOfSubs
        return ans
        
