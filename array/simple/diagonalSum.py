# 矩阵对角线元素的和
# https://leetcode.cn/problems/matrix-diagonal-sum/
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        ans = 0
        for i in range(size):
            ans += mat[i][i]
            j = size - 1 - i
            if i != j:
                ans += mat[j][i]
        return ans


s = Solution()
assert s.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
assert s.diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8
