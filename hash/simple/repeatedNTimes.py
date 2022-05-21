# 在长度 2N 的数组中找出重复 N 次的元素
# https://leetcode.cn/problems/n-repeated-element-in-size-2n-array/
import random
from typing import List


class Solution:

    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            x, y = random.randrange(n), random.randrange(n)
            if x != y and nums[x] == nums[y]:
                return nums[x]

    def repeatedNTimes2(self, nums: List[int]) -> int:
        n = len(nums)
        for step in [1, 2, 3]:
            for i in range(n - step):
                if nums[i] == nums[i + step]:
                    return nums[i]
        return -1

    def repeatedNTimes3(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
        return -1


s = Solution()
assert s.repeatedNTimes([8, 3, 2, 3]) == 3
assert s.repeatedNTimes([1, 2, 3, 3]) == 3
assert s.repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2
assert s.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5
