#  跳跃游戏 II
# https://leetcode.cn/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


s = Solution()
assert s.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]) == 2
assert s.jump([1, 2, 1, 1, 1]) == 3
assert s.jump([2, 3, 1]) == 1
assert s.jump([2, 1]) == 1
assert s.jump([2, 3, 1, 1, 4]) == 2
assert s.jump([2, 3, 0, 1, 4]) == 2
