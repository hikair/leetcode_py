# 查找和替换模式
# https://leetcode.cn/problems/find-and-replace-pattern/
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str, pattern: str):
            map = {}
            for x, y in zip(word, pattern):
                if x not in map:
                    map[x] = y
                    continue
                if map[x] != y:
                    return False
            return True

        return [word for word in words if match(word, pattern) and match(pattern, word)]


s = Solution()
print(s.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
