# 二进制求和
# https://leetcode-cn.com/problems/add-binary/
class Solution:
    def addBinary(self, a, b):
        res = ""
        r = 0
        sizeA = len(a)
        sizeB = len(b)
        size = max(sizeA, sizeB)
        for i in range(1, size + 1):
            temp = r
            if i <= sizeA:
                temp += int(a[-i])
            if i <= sizeB:
                temp += int(b[-i])
            if temp > 1:
                res = str(temp % 2) + res
                r = 1
            else:
                res = str(temp) + res
                r = 0
        return res if r == 0 else "1" + res


s = Solution()
print(s.addBinary("11", "1")) # 100
print(s.addBinary("1010", "1011")) # 10101
print(s.addBinary("111", "111")) # 1110
