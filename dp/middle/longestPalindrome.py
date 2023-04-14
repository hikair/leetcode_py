# 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        l, r = 0, 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for step in range(1, n):
            for i in range(n - step):
                if step == 1 or dp[i + 1][i + step - 1]:
                    dp[i][i + step] = s[i] == s[i + step]
                if dp[i][i + step] and r - l < step:
                    l, r = i, i + step
        return s[l:r + 1]


s = Solution()
assert s.longestPalindrome('babad') == 'bab'
assert s.longestPalindrome('a') == 'a'
assert s.longestPalindrome('aaaaa') == 'aaaaa'