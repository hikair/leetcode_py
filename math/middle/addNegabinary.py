# 1073. 负二进制数相加
# https://leetcode.cn/problems/adding-two-negabinary-numbers/
from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sum = 0
        for i, v in enumerate(arr1[::-1]):
            sum += (-2) ** i if v == 1 else 0
        for i, v in enumerate(arr2[::-1]):
            sum += (-2) ** i if v == 1 else 0

        def baseNeg2(n: int) -> List[int]:
            if n == 0:
                return [0]
            ans = []
            while n != 0:
                a = abs(n % (-2))
                ans.append(a)
                n = (n - a) // -2
            return ans[::-1]
        return baseNeg2(sum)


s = Solution()
assert s.addNegabinary([0], [1, 0]) == [1, 0]
assert s.addNegabinary([1, 1, 1, 1, 1], [1, 0, 1]) == [1, 0, 0, 0, 0]
assert s.addNegabinary([0], [0]) == [0]
assert s.addNegabinary([0], [1]) == [1]
