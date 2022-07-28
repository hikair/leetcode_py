# 有效的正方形
# https://leetcode.cn/problems/valid-square/
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def len(a: List[int], b: List[int]) -> int:
            return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])

        l = [len(p1, p2), len(p1, p3), len(p1, p4), len(p2, p3), len(p2, p4), len(p3, p4)]
        l.sort()
        return l[0] == l[1] and l[0] == l[2] and l[0] == l[3] and l[4] == l[5] and l[0] > 0


s = Solution()
assert s.validSquare([0, 0], [1, 1], [1, 0], [0, 1])
assert not s.validSquare([0, 0], [1, 1], [1, 0], [0, 12])
assert s.validSquare([1, 0], [-1, 0], [0, 1], [0, -1])
assert not s.validSquare([0, 0], [0, 0], [0, 0], [0, 0])