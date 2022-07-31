# 生成每种字符都是奇数个的字符串
# https://leetcode.cn/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
    def generateTheString(self, n: int) -> str:
        return 'a' * n if n & 1 == 1 else 'a' * (n - 1) + 'b'


s = Solution()
assert s.generateTheString(3) == 'aaa'
assert s.generateTheString(4) == 'aaab'