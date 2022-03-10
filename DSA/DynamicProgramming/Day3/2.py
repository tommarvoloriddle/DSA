"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        maxUntilNow = [-1]*(len(nums) + 1)
        n1 = []
        for i in range(1, len(nums)):
            n1.append(nums[i])
        n2 = []
        for i in range(0, len(nums)-1):
            n2.append(nums[i])
        n = len(nums)
        nums.append(0)
        maxUntilNow[0] = nums[0]
        if nums[1]:
            maxUntilNow[1] = max(nums[0], nums[1])

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


        m1 = [-1]*(len(n1) + 1)
        n = len(n1)
        n1.append(0)
        m1[0] = n1[0]
        if n1[1]:
            m1[1] = max(n1[0], n1[1])

        def h1(n):
            if m1[n] != -1:
                return m1[n]
            else:
                if m1[n-1] == -1:
                    m1[n-1] = h1(n-1)
                if n-2 < 0:
                    m1[n] = m1[n-1]
                    return m1[n-1]
                if m1[n-2] == -1:
                    m1[n-2] = h1(n-2)
                m1[n] = max(m1[n-1], m1[n-2]+n1[n])
                return m1[n]
        h1(n)


        m2 = [-1]*(len(nums) + 1)
        n = len(n2)
        n2.append(0)
        m2[0] = n2[0]
        if n2[1]:
            m2[1] = max(n2[0], n2[1])

        def h2(n):
            if m2[n] != -1:
                return m2[n]
            else:
                if m2[n-1] == -1:
                    m2[n-1] = h2(n-1)
                if n-2 < 0:
                    m2[n] = m2[n-1]
                    return m2[n-1]
                if m2[n-2] == -1:
                    m2[n-2] = h2(n-2)
                m2[n] = max(m2[n-1], m2[n-2]+n2[n])
                return m2[n]
        h2(n)
        # print(maxUntilNow, m1, m2)
        # print(nums, n1, n2)
        return min(max(max(m1), max(m2)), max(maxUntilNow))
