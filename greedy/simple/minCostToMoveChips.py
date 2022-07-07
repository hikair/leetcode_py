# 玩筹码
# https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        for i in position:
            if (i & 1) == 0:
                even += 1
        return min(even, len(position) - even)


s = Solution()
assert s.minCostToMoveChips([1, 2, 3]) == 1
assert s.minCostToMoveChips([2, 2, 2, 3, 3]) == 2
assert s.minCostToMoveChips([1, 1000000000]) == 1