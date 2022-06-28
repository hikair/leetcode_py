# 最接近的三数之和
# https://leetcode.cn/problems/3sum-closest/
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n, ans = len(nums), 100000
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = n - 1
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while k > j and nums[i] + nums[j] + nums[k] > target:
                    t = nums[i] + nums[j] + nums[k] - target
                    if abs(t) < abs(ans):
                        ans = t
                    k -= 1
                if j == k:
                    break
                t = nums[i] + nums[j] + nums[k] - target
                if t == 0:
                    return target
                if abs(t) < abs(ans):
                    ans = t
        return target + ans


s = Solution()
assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2
assert s.threeSumClosest([0, 0, 0], 1) == 0
