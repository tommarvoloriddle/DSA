"""
ou are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.



Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2


Constraints:

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000
:"""
import math
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        a = [0]*(n)
        b = [0]*(n)
        a[0] = values[0]
        for i in range(1, n):
            a[i] = max(a[i-1], (values[i] + i))

        b[n-1] = (values[n-1] - (n-1))

        for j in range(n-2, -1, -1):
            b[j] = max(b[j+1] , (values[j] - j))
        ans  = -math.inf
        for i in range(0, n-1):
            if (a[i] + b[i+1]) > ans:
                ans = a[i] + b[i+1]
        # print(a, b)
        return ans
