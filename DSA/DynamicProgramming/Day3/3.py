
"""
\You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.



Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = {}

        for i in range(0, len(nums)):
            if nums[i] in d.keys():
                d[nums[i]] += nums[i]
            else:
                d[nums[i]] = nums[i]

        w = [0]


        for i in range(1, 20002):
            if i in d.keys():
                w.append(d[i])
            else:
                w.append(0)
        nums = w
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
            
