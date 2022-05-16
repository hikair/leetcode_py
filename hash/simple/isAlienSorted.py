# 验证外星语词典
# https://leetcode.cn/problems/verifying-an-alien-dictionary/
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        size = len(words)
        for i in range(size - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                t = order.index(words[i][j]) - order.index(words[i + 1][j])
                if t > 0:
                    return False
                if t < 0:
                    break
        return True


s = Solution()
assert s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
assert not s.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
assert not s.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz")