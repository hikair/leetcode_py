# threeSum
# https://leetcode.cn/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, ans = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            r = n - 1
            for j in range(i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while j < r and nums[i] + nums[j] + nums[r] > 0:
                    r -= 1
                if j == r:
                    break
                if nums[i] + nums[j] + nums[r] == 0:
                    ans.append([nums[i], nums[j], nums[r]])
        return ans


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4])) # [[-1,-1,2],[-1,0,1]]
print(s.threeSum([])) # []
print(s.threeSum([0])) # []