# 打家劫舍
# https://leetcode.cn/problems/house-robber/
from typing import List


class Solution:
    # 只有一件房间，dp[0] = nums[0]
    # 只有两间房间，dp[1] = max(nums[0], nums[1])
    # 超过两个房间：设当前房间为k
    #   1.偷当前房间，那么第k-1间房间不能偷，dp[k] = dp[k - 2] + nums[k]
    #   2.不偷当前房间，dp[k] = dp[k - 1]
    # 那么转移方程为：dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    # dp[i]表示第i间房间最多可偷金额
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]


s = Solution()
assert s.rob([0]) == 0
assert s.rob([2, 1, 1, 2]) == 4
assert s.rob([1, 2, 3, 1]) == 4
assert s.rob([2, 7, 9, 3, 1]) == 12
