# 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for x in range(n + 1)]
        dp[0], dp[1] = [""], ["()"]
        for i in range(2, n + 1):
            for j in range(i):
                for inner in dp[j]:
                    for outer in dp[i - j - 1]:
                        dp[i].append("({}){}".format(inner, outer))
        return dp[n]

s = Solution()
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
