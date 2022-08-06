# 数组中的字符串匹配
# https://leetcode.cn/problems/string-matching-in-an-array/
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        ans, n = [], len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans


s = Solution()
assert s.stringMatching(["leetcoder", "leetcode", "od", "hamlet", "am"]) == ["od", "am", "leetcode"]
