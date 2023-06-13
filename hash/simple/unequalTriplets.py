# https://leetcode.cn/problems/number-of-unequal-triplets-in-array/
# 2475. 数组中不等三元组的数目
from typing import List
from collections import Counter

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans, t, l = 0, 0, len(nums)
        for k, v in c.items():
            ans += t * v * (l - t - v)
            t += v
        return ans


s = Solution()
assert s.unequalTriplets([4, 4, 2, 4, 3]) == 3
assert s.unequalTriplets([1, 1, 1, 1, 1]) == 0