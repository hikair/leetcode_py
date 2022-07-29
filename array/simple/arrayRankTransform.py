# 数组序号转换
# https://leetcode.cn/problems/rank-transform-of-an-array/
from typing import List

from sortedcontainers import SortedDict


class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[v] for v in arr]

    def arrayRankTransform2(self, arr: List[int]) -> List[int]:
        map = SortedDict()
        for i in arr:
            map[i] = 0
        index = 1
        for key in map.keys():
            map[key] = index
            index += 1
        for i in range(len(arr)):
            arr[i] = map[arr[i]]
        return arr


s = Solution()
assert s.arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]
assert s.arrayRankTransform([100, 100, 100]) == [1, 1, 1]
assert s.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]) == [5, 3, 4, 2, 8, 6, 7, 1, 3]
