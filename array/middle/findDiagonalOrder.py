# 对角线遍历
# https://leetcode.cn/problems/diagonal-traverse/
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n, ans = len(mat), len(mat[0]), []
        for i in range(0, m + n):
            if i % 2 == 0:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    ans.append(mat[x][y])
                    x -= 1
                    y += 1
            else:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while y >= 0 and x < m:
                    ans.append(mat[x][y])
                    x += 1
                    y -= 1
        return ans


s = Solution()
assert s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
assert s.findDiagonalOrder([[1, 2], [3, 4]]) == [1, 2, 3, 4]
