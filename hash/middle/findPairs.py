# 数组中的 k-diff 数对
# https://leetcode.cn/problems/k-diff-pairs-in-an-array/
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans, visited = set(), set()
        for num in nums:
            if num - k in visited:
                ans.add(num - k)
            if num + k in visited:
                ans.add(num)
            visited.add(num)
        return len(ans)


s = Solution()
assert s.findPairs([3, 1, 4, 1, 5], 2) == 2
assert s.findPairs([1, 2, 3, 4, 5], 1) == 4
assert s.findPairs([1, 3, 1, 5, 4], 0) == 1