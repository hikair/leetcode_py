# 数组中重复的数据
# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            val = abs(num)
            if nums[val - 1] > 0:
                nums[val - 1] = -nums[val - 1]
            else:
                ans.append(val)
        return ans