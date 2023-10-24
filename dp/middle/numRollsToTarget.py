# 1155. 掷骰子等于目标和的方法数

class Solution:

    mod = 1000000007

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        for i in range(1, min(k, target) + 1):
            dp[1][i] = 1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                for l in range(1, target - j + 1):
                     dp[i][l + j] = (dp[i][l + j] + dp[i - 1][l]) % self.mod
        return dp[n][target]

s = Solution()
assert s.numRollsToTarget(3, 6, 7) == 15
assert s.numRollsToTarget(2, 12, 8) == 7
assert s.numRollsToTarget(1, 6, 3) == 1
assert s.numRollsToTarget(2, 6, 7) == 6
assert s.numRollsToTarget(30, 30, 500) == 222616187