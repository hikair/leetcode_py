# 环绕字符串中唯一的子字符串
# https://leetcode.cn/problems/unique-substrings-in-wraparound-string/

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [0 for _ in range(26)]
        n, count = len(p), 0
        for i in range(n):
            if i > 0 and (ord(p[i]) - ord(p[i - 1] ) + 26) % 26 == 1:
                count += 1
            else:
                count = 1
            dp[ord(p[i]) - ord('a')] = max(count, dp[ord(p[i]) - ord('a')])
        return sum(dp)


s = Solution()
assert s.findSubstringInWraproundString('a') == 1
assert s.findSubstringInWraproundString('cac') == 2
assert s.findSubstringInWraproundString('zab') == 6