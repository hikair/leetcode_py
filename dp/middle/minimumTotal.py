# 三角形最小路径和
# https://leetcode.cn/problems/triangle/
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            m = len(triangle[i])
            for j in range(m):
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                elif j == m - 1:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1])
                dp[i][j] += triangle[i][j]
        return min(dp[n - 1])


s = Solution()
assert s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
assert s.minimumTotal([[2], [3, 4], [6, 5, 9], [4, 4, 8, 0]]) == 14
assert s.minimumTotal([[-10]]) == -10
