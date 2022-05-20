# 寻找右区间
# https://leetcode.cn/problems/find-right-interval/
import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        size = len(intervals)
        map = dict([(intervals[i][0], i) for i in range(size)])
        start = [x[0] for x in intervals]
        start.sort()
        ans = [-1 for _ in range(size)]
        for x, y in intervals:
            index = bisect.bisect_left(start, y)
            if index < size:
                ans[map[x]] = map[start[index]]
        return ans

    def findRightInterval2(self, intervals: List[List[int]]) -> List[int]:
        size = len(intervals)
        map = dict([(intervals[i][0], i) for i in range(size)])
        ans = [-1 for _ in range(size)]
        intervals.sort()
        for i in range(size):
            target = intervals[i][1]
            l = 0
            r = size
            while l < r:
                m = l + (r - l) // 2
                if intervals[m][0] >= target:
                    r = m
                else:
                    l = m + 1
            if l < size:
                ans[map[intervals[i][0]]] = map[intervals[l][0]]
        return ans


s = Solution()
assert s.findRightInterval([[1, 1], [3, 4]]) == [0, -1]
assert s.findRightInterval([[1, 2]]) == [-1]
assert s.findRightInterval([[3, 4], [2, 3], [1, 2]]) == [-1, 0, 1]
assert s.findRightInterval([[1, 4], [2, 3], [3, 4]]) == [-1, 2, -1]
