# 四数之和
# https://leetcode.cn/problems/4sum/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n, ans = len(nums), []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = n - 1
                for k in range(j + 1, n - 1):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    while t > k and nums[i] + nums[j] + nums[k] + nums[t] > target:
                        t -= 1
                    if t == k:
                        break
                    if nums[i] + nums[j] + nums[k] + nums[t] == target:
                        ans.append([nums[i], nums[j], nums[k], nums[t]])
        return ans


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(s.fourSum([2, 2, 2, 2, 2], 8)) # [2,2,2,2,2]
