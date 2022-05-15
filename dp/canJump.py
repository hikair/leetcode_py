# 跳跃游戏
# https://leetcode.cn/problems/jump-game/
from typing import List


class Solution:
    # dp[x] = 遍历[0, x - 1] : dp[i] and nums[i] >= x - i
    # 实际会超时，建议用贪心来做
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        dp = [False for _ in range(size)]
        dp[0] = True
        for i in range(1, size):
            for j in range(i):
                if dp[j] and nums[j] >= i - j:
                    dp[i] = True
                    break
        return dp[size - 1]


s = Solution()
assert s.canJump([2, 3, 1, 1, 4])
assert not s.canJump([3, 2, 1, 0, 4])