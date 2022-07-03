# 下一个排列
# https://leetcode.cn/problems/next-permutation/
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n, a = len(nums), -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                a = i - 1
                break
        if a >= 0:
            for i in range(n - 1, a, -1):
                if nums[i] > nums[a]:
                    nums[i], nums[a] = nums[a], nums[i]
                    break
        # 反转[a + 1, n)
        l, r = a + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


s = Solution()
nums = [1, 2, 3]
s.nextPermutation(nums)
assert nums == [1, 3, 2]
