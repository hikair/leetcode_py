# 最小绝对差
# https://leetcode.cn/problems/minimum-absolute-difference/
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff, n, ans = arr[1] - arr[0], len(arr), []
        for i in range(2, n):
            diff = min(diff, arr[i] - arr[i - 1])
            if diff == 1:
                break
        for i in range(1, n):
            if arr[i] - arr[i - 1] == diff:
                ans.append([arr[i - 1], arr[i]])
        return ans


s = Solution()
print(s.minimumAbsDifference([4, 2, 1, 3])) # [1, 2], [2, 3], [3, 4]