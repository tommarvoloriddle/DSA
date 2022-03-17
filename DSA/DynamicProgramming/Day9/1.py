"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Accepted
1,025,080
Submissions
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {}
        for word in wordDict:
            d[word] = 1
        n = len(s)
        matrix = [-1] * (n + 1)

        matrix[0] = 1


        for i in range(0, n):

            for j in range(i+1, n+1):
                currentSubstr = s[i:j]
                # print(currentSubstr)
                if matrix[i] == 1 and currentSubstr in d.keys():
                    # print(i, j,"found")
                    matrix[j] = 1
        # print(matrix)
        if matrix[-1] == -1:
            return False
        return True
