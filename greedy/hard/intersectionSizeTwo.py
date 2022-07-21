# 设置交集大小至少为2
# https://leetcode.cn/problems/set-intersection-size-at-least-two/
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 右边界升序，左边界降序
        intervals.sort(key=lambda x: (x[1], -x[0]))
        ans, end = 2, intervals[0][1],
        pre_end = end - 1
        for x, y in intervals[1:]:
            if x <= pre_end:
                continue
            if x <= end:
                ans += 1
                pre_end = end
                end = y
            else:
                ans += 2
                pre_end = y - 1
                end = y
        return ans


s = Solution()
assert s.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]) == 3
assert s.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]) == 5
