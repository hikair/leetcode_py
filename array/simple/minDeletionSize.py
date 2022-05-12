# 删列造序
# https://leetcode.cn/problems/delete-columns-to-make-sorted/
from typing import List

from more_itertools import pairwise


class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(x > y for x, y in pairwise(col)) for col in zip(*strs))

    def minDeletionSize2(self, strs: List[str]) -> int:
        col, row, ans = len(strs[0]), len(strs), 0
        for i in range(col):
            for j in range(row - 1):
                if ord(strs[j][i]) - ord(strs[j + 1][i]) > 0:
                    ans += 1
                    break
        return ans


s = Solution()
print(s.minDeletionSize(["cba", "daf", "ghi"]))  # 1
print(s.minDeletionSize(["a", "b"]))  # 0
print(s.minDeletionSize(["zyx", "wvu", "tsr"]))  # 3
