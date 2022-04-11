# 统计各位数字都不同的数字个数
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        dp = [1, 10]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + (dp[i - 1] - dp[i - 2]) * (11 - i))
        return dp[n]


s = Solution()
print(s.countNumbersWithUniqueDigits(0)) # 0
print(s.countNumbersWithUniqueDigits(1)) # 10
print(s.countNumbersWithUniqueDigits(2)) # 91