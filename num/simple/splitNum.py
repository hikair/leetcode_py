# 最小和分割
# https://leetcode.cn/problems/split-with-minimum-sum

class Solution:
    def splitNum(self, num: int) -> int:
        s = "".join(sorted(str(num)))
        num1, num2 = int(s[::2]), int(s[1::2])
        return num1 + num2

s = Solution()
assert s.splitNum(4325) == 59