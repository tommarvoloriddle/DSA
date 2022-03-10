"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        isReachable = [-1]*(len(nums) + 1)
        isReachable[0] = 1
        if len(nums) == 1:
            return True
        if nums[0] <= 0:
            return False
        n = len(nums)
        # isReachable[n] = 1
        dis = 0
        r = n-1
        l = 0

        idx = n - 1
        j = idx - 1
        ans = False
        while idx > 1 and j >= 0:
            # print(idx, j)
            if nums[j] != 0:
                if nums[j] >= (idx - j):
                    idx = j
                    j = idx - 1
                else:
                    j = j - 1
            else:
                j = j - 1
        if j <= 0 and idx <= 1:
            return True
        return False
