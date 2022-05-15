# 跳跃游戏
# https://leetcode.cn/problems/jump-game/
from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        max_len = 0
        for i, j in enumerate(nums):
            if max_len < i:
                return False
            max_len = max(max_len, i + j)
        return True


s = Solution()
assert s.canJump([2, 3, 1, 1, 4])
assert not s.canJump([3, 2, 1, 0, 4])
