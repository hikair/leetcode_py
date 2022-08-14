# 1422. 分割字符串的最大得分

class Solution:
    def maxScore(self, s: str) -> int:
        ans = score = (s[0] == '0') + s[1:].count('1')
        for c in s[1:-1]:
            score += 1 if c == '0' else -1
            ans = max(ans, score)
        return ans


s = Solution()
assert s.maxScore('011101') == 5
assert s.maxScore('00111') == 5
assert s.maxScore('1111') == 3