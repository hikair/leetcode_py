# 全排列
# https://leetcode.cn/problems/permutations/
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(nums, temp):
            if not nums:
                ans.append(temp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], temp + [nums[i]])
        backtrack(nums, [])
        return ans

    def permute2(self, nums: List[int]) -> List[List[int]]:
        size, ans, path = len(nums), [], []
        used = [False for _ in range(size)]

        def backtrack():
            for i, j in enumerate(nums):
                if used[i]:
                    continue
                path.append(j)
                used[i] = True
                if len(path) == size:
                    ans.append(list(path))
                backtrack()
                used[i] = False
                path.pop()
        backtrack()
        return ans


s = Solution()
print(s.permute([1, 2, 3]))
