# 不同路径 II
# https://leetcode.cn/problems/unique-paths-ii/
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


s = Solution()
obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
assert s.uniquePathsWithObstacles([[0,1],[0,0]]) == 1
