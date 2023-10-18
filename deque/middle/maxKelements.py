# 2530. 执行 K 次操作后的最大分数
# https://leetcode.cn/problems/maximal-score-after-applying-k-operations/description
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = [-x for x in nums]
        heapify(q)
        ans = 0
        for _ in range(k):
            t = heappop(q)
            ans -= t
            heappush(q, -((-t + 2) // 3))
        return ans


s = Solution()
assert s.maxKelements([238838724, 196963851, 539418658, 120132686, 273213807, 57187185, 68854249, 619718192],
                      7) == 2254532183
assert s.maxKelements([1, 10, 3, 3, 3], 3) == 17
