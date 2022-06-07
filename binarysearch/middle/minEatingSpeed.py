# 爱吃香蕉的珂珂
# https://leetcode.cn/problems/koko-eating-bananas/
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            speed = l + (r - l) // 2
            cost = sum([ceil(x / speed) for x in piles])
            if cost > h:
                l = speed + 1
            else:
                r = speed
        return l


s = Solution()
assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
