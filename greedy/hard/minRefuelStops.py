# 最低加油次数
# https://leetcode.cn/problems/minimum-number-of-refueling-stops/
from typing import List

import heapq


class Solution:

    # heapq只能构建小根堆，可以将stations[i][1]变为相反数
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n, prev, count, fuel, h = len(stations), 0, 0, startFuel, []
        for i in range(n + 1):
            cur = stations[i][0] if i < n else target
            fuel -= cur - prev
            while fuel < 0 and h:
                fuel -= heapq.heappop(h)
                count += 1
            if fuel < 0:
                return -1
            if i < n:
                heapq.heappush(h, -stations[i][1])
                prev = cur
        return count


s = Solution()
assert s.minRefuelStops(100, 50, [[25, 30]]) == -1
assert s.minRefuelStops(1, 1, []) == 0
assert s.minRefuelStops(100, 1, [[10, 100]]) == -1
assert s.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2
