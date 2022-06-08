# 有效的回旋镖
# https://leetcode.cn/problems/valid-boomerang/
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        ab = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
        ac = [points[2][0] - points[0][0], points[2][1] - points[0][1]]
        return ab[1] * ac[0] != ab[0] * ac[1]


s = Solution()
assert s.isBoomerang([[1, 1], [2, 3], [3, 2]])
assert not s.isBoomerang([[1, 1], [2, 2], [3, 3]])
