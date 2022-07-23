# 公交站间的距离
# https://leetcode.cn/problems/distance-between-bus-stops/
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        sum, x, n = 0, 0, len(distance)
        for i in range(n):
            sum += distance[i]
            if i in range(start, destination):
                x += distance[i]
        return min(x, sum - x)


s = Solution()
assert s.distanceBetweenBusStops([1, 2, 3, 4], 0, 1) == 1
assert s.distanceBetweenBusStops([1, 2, 3, 4], 0, 2) == 3
assert s.distanceBetweenBusStops([1, 2, 3, 4], 0, 3) == 4