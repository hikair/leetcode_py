# 全排列 II
# https://leetcode.cn/problems/permutations-ii/
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        size, ans, path = len(nums), [], []
        used = [False for _ in range(size)]
        nums.sort()

        def backtrack():
            if len(path) == size:
                ans.append(list(path))
                return
            for i in range(size):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i  - 1]):
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return ans


s = Solution()
print(s.permuteUnique([1, 1, 2]))
print(s.permuteUnique([1, 2, 3]))