# 最大三角形面积
# https://leetcode.cn/problems/largest-triangle-area/
from itertools import combinations
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        s = 0.0
        for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
            s = max(s, abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) * 0.5)
        return s

    def largestTriangleArea2(self, points: List[List[int]]) -> float:
        size = len(points)
        s = 0.0
        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    x1 = points[i][0]
                    x2 = points[j][0]
                    x3 = points[k][0]
                    y1 = points[i][1]
                    y2 = points[j][1]
                    y3 = points[k][1]
                    s = max(s, abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) * 0.5)
        return s


s = Solution()
assert s.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]) - 2.0 == 0
