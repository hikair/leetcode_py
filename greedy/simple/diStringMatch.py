# 增减字符串匹配
# https://leetcode.cn/problems/di-string-match/
from typing import List


class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        ans = []
        for c in s:
            if c == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        ans.append(low)
        return ans


s = Solution()
print(s.diStringMatch("IDID"))
print(s.diStringMatch("III"))
print(s.diStringMatch("DII"))