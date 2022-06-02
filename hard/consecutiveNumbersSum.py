# 连续整数求和
# https://leetcode.cn/problems/consecutive-numbers-sum/

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans, i = 0, 1
        while n > 0:
            ans += (n % i == 0)
            n -= i
            i += 1
        return ans


s = Solution()
assert s.consecutiveNumbersSum(5) == 2
assert s.consecutiveNumbersSum(9) == 3
assert s.consecutiveNumbersSum(15) == 4