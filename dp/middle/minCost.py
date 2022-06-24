# 粉刷房子
# https://leetcode.cn/problems/JEj789/
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        m = len(costs)
        for i in range(1, m):
            costs[i][0] = costs[i][0] + min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] = costs[i][1] + min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] = costs[i][2] + min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[m - 1])


s = Solution()
assert s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10
assert s.minCost([[7, 6, 2]]) == 2
