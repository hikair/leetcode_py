# 摆动排序 II
# https://leetcode.cn/problems/wiggle-sort-ii/
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        x = (n + 1) // 2
        t = sorted(nums)
        j, k = x - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = t[j]
            if i + 1 < n:
                nums[i + 1] = t[k]
            j -= 1
            k -= 1


s = Solution()
nums = [1, 5, 1, 1, 6, 4]
s.wiggleSort(nums)
print(nums)
