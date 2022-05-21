# 不同路径
# https://leetcode.cn/problems/unique-paths/

class Solution:
    # dp[i][j]表示有x种方案到达(i, j)
    # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


s = Solution()
assert s.uniquePaths(3, 7) == 28
assert s.uniquePaths(3, 2) == 3