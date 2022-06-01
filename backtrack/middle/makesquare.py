# 火柴拼正方形
# https://leetcode.cn/problems/matchsticks-to-square/
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        size, total = len(matchsticks), sum(matchsticks)
        if total % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        edg = total / 4
        if matchsticks[-1] > edg:
            return False
        lens = [0] * 4

        def backtrack(index):
            if index == size:
                return lens[0] == edg and lens[0] == lens[1] and lens[1] == lens[2]
            for i in range(4):
                if lens[i] + matchsticks[index] > edg:
                    continue
                lens[i] += matchsticks[index]
                if backtrack(index + 1):
                    return True
                lens[i] -= matchsticks[index]
            return False

        return backtrack(0)


s = Solution()
assert s.makesquare([1, 1, 2, 2, 2])
assert not s.makesquare([3, 3, 3, 3, 4])
