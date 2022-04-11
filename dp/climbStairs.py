# 爬楼梯
# https://leetcode-cn.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


s = Solution()
print(s.climbStairs(2)) # 2
print(s.climbStairs(3)) # 3
print(s.climbStairs(4)) # 5