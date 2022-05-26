# 比特位计数
# https://leetcode.cn/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

    def countBits2(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        high = 0
        for i in range(1, n + 1):
            if (i & (i - 1)) == 0:
                high = i
            dp[i] = dp[i - high] + 1
        return dp
