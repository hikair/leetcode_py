# 将字符串翻转到单调递增
# https://leetcode.cn/problems/flip-string-to-monotone-increasing/

class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for c in s:
            dp1 = min(dp0, dp1) + ord('1') - ord(c)
            dp0 += ord(c) - ord('0')
        return min(dp0, dp1)

    def minFlipsMonoIncr2(self, s: str) -> int:
        n = len(s)
        dp = [[0, 0] for _ in range(n)]
        if s[0] == '0':
            dp[0][1] = 1
        else:
            dp[0][0] = 1
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + ord(s[i]) - ord('0')
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + ord('1') - ord(s[i])
        return min(dp[n - 1][0], dp[n - 1][1])


s = Solution()
assert s.minFlipsMonoIncr('00110') == 1
assert s.minFlipsMonoIncr('010110') == 2
assert s.minFlipsMonoIncr('00011000') == 2
