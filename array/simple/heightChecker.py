# 高度检查器
# https://leetcode.cn/problems/height-checker/
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        m, ans, index = max(heights), 0, 0
        arr = [0] * (m + 1)
        for height in heights:
            arr[height] += 1
        for i in range(1, m + 1):
            while arr[i] > 0:
                arr[i] -= 1
                if i != heights[index]:
                    ans += 1
                index += 1
        return ans


s = Solution()
assert s.heightChecker([1, 1, 4, 2, 1, 3]) == 3
assert s.heightChecker([5, 1, 2, 3, 4]) == 5
assert s.heightChecker([1, 2, 3, 4, 5]) == 0
