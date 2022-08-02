# 有序队列
# https://leetcode.cn/problems/orderly-queue/

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        return min(s[i:] + s[:i] for i in range(len(s))) if k == 1 else ''.join(sorted(s))


s = Solution()
assert s.orderlyQueue('cba', 1) == 'acb'
assert s.orderlyQueue('baaca', 3) == 'aaabc'