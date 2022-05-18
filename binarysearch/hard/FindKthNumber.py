# 乘法表中第k小的数
# https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 0, m * n
        while l < r:
            x = l + (r - l) // 2
            count = x // n * n
            for i in range(x // n + 1, m + 1):
                count += x // i
            if count < k:
                l = x + 1
            else:
                r = x
        return l


s = Solution()
assert s.findKthNumber(3, 3, 5) == 3
assert s.findKthNumber(2, 3, 6) == 6