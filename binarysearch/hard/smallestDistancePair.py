# 找出第 K 小的数对距离
# https://leetcode.cn/problems/find-k-th-smallest-pair-distance/
from typing import List
import bisect


class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, nums[n - 1]
        while l <= r:
            mid = l + (r - l) // 2
            count = 0
            for i in range(n):
                j = bisect.bisect_left(nums[:i], nums[i] - mid)
                count += i - j
            if count >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l


s = Solution()
assert s.smallestDistancePair([1, 3, 1], 1) == 0
assert s.smallestDistancePair([1, 1, 1], 2) == 0
assert s.smallestDistancePair([1, 6, 1], 3) == 5
