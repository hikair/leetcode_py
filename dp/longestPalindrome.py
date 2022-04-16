# 最长回文串
# https://leetcode-cn.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        rl = rr = 0
        for i in range(length):
            left = right = i
            while left > 0 and s[left - 1] == s[i]:
                left -= 1
            while right < length - 1 and s[right + 1] == s[i]:
                right += 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left > rr - rl:
                rl = left
                rr = right
        return s[rl+1:rr]

    def longestPalindrome2(self, s: str) -> str:
        length = len(s)
        dp = [[bool(i - j == 0) for j in range(length)] for i in range(length)]
        rl = rr = 0
        for step in range(2, length + 1):
            for i in range(length):
                j = i + step - 1
                if j >= length:
                    break
                if step == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and (step > rr - rl):
                    rl = i
                    rr = j
        return s[rl:rr + 1]


s = Solution()
a  = "aba"

print(s.longestPalindrome("aba")) # aba
print(s.longestPalindrome("bb")) # bb
print(s.longestPalindrome("babad")) # aba bab
print(s.longestPalindrome("cbbd")) # bb
print(s.longestPalindrome("acbbcd")) # cbbc