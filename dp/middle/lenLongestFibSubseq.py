# 最长的斐波那契子序列的长度
# https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n, ans = len(arr), 0
        indexMap = {j: i for i, j in enumerate(arr)}
        dp = [[0] * n for _ in range(n)]
        for i in range(2, n):
            for j in range(i - 1, 0, -1):
                if arr[j] * 2 <= arr[i]:
                    break
                v = arr[i] - arr[j]
                k = -1 if v not in indexMap else indexMap[v]
                if k > -1:
                    dp[j][i] = max(dp[k][j] + 1, 3)
                    ans = max(ans, dp[j][i])
        return ans


s = Solution()
# assert s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]) == 5
# assert s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]) == 3
assert s.lenLongestFibSubseq([2392, 2545, 2666, 5043, 5090, 5869, 6978, 7293, 7795]) == 0
