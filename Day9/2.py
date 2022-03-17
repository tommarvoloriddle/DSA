
"""
 42. Trapping Rain Water
Hard

17264

243

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
Accepted
1,058,369
Submissions
1,888,973
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        a = height
        n = len(a)
        l = [0]*n
        r = [0]*n
        maxi = -1
        for i in range(0, n):
            maxi = max(a[i], maxi)
            l[i] = maxi
        maxi = -1
        for i in range(n-1, -1, -1):
            maxi = max(a[i], maxi)
            r[i] = maxi

        # print(l, r)
        ans = 0
        for i in range(0, n):
            ans= ans + ( min(l[i], r[i]) - a[i] )
        return ans
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left, right = 0, n - 1
        l_max, r_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                l_max = max(l_max,height[left])
                ans = ans + l_max - height[left]
                left = left + 1
            else:
                r_max = max(r_max,height[right])
                ans = ans + r_max - height[right]
                right = right - 1
        return ans
