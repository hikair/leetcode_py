# 加一
# https://leetcode-cn.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):
        r = 1
        b = []
        for i in digits[::-1]:
            if i + r > 9:
                b.insert(0, 0)
            else:
                b.insert(0, i + r)
                r = 0
        if r == 1:
            b.insert(0, 1)
        return b


s = Solution()
print(s.plusOne([1, 2, 3])) # [1, 2, 4]
print(s.plusOne([4, 3, 2, 1])) # [4, 3, 2, 2]
print(s.plusOne([0])) # [1]
print(s.plusOne([9, 9, 9])) # [1, 0, 0, 0]