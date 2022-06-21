# 盛最多水的容器
# https://leetcode.cn/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area


s = Solution()
assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49