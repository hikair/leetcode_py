# 非递增顺序的最小子序列
# https://leetcode.cn/problems/minimum-subsequence-in-non-increasing-order/
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total, cur = sum(nums), 0

        for i, v in enumerate(nums):
            cur += v
            if 2 * cur > total:
                return nums[:i + 1]


s = Solution()
assert s.minSubsequence([4, 3, 10, 9, 8]) == [10, 9]
assert s.minSubsequence([4, 4, 7, 6, 7]) == [7, 7, 6]
assert s.minSubsequence([6]) == [6]
assert s.minSubsequence([8, 8]) == [8, 8]
