# 最少移动次数使数组元素相等 II
# https://leetcode.cn/problems/minimum-moves-to-equal-array-elements-ii/
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(num - mid) for num in nums)


s = Solution()
# assert s.minMoves2([1, 2, 3]) == 2
assert s.minMoves2([1, 10, 2, 9]) == 16