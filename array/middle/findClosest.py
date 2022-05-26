# 面试题 17.11. 单词距离
# https://leetcode.cn/problems/find-closest-lcci/
from typing import List


class Solution:

    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        a, b = -1, -1
        ans = len(words)
        for i, j in enumerate(words):
            if j == word1:
                a = i
            if j == word2:
                b = i
            if a > 0 and b > 0:
                ans = min(abs(a - b), ans)
        return ans

    def findClosest2(self, words: List[str], word1: str, word2: str) -> int:
        a, b = [], []
        for i, j in enumerate(words):
            if j == word1:
                a.append(i)
            if j == word2:
                b.append(i)
        ans = len(words)
        for i in a:
            for j in b:
                ans = min(abs(i - j), ans)
        return ans


words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
s = Solution()
assert s.findClosest(words, 'a', 'student') == 1
