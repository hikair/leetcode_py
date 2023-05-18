# 1017. 负二进制转换
# https://leetcode.cn/problems/convert-to-base-2/

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        ans = ''
        while n != 0:
            a = abs(n % (-2))
            ans += str(a)
            n = (n - a) // -2
        return str(ans[::-1])


s = Solution()
assert s.baseNeg2(2) == '110'
assert s.baseNeg2(3) == '111'
assert s.baseNeg2(4) == '100'
