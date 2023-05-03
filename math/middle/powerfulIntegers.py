# 强整数
# https://leetcode.cn/problems/powerful-integers/
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        v1 = 1
        for i in range(21):
            v2 = 1
            for j in range(21):
                v = v1 + v2
                if v > bound:
                    break
                v2 *= y
                ans.add(v)
            if v1 > bound:
                break
            v1 *= x
        return list(ans)