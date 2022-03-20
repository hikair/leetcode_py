# https://leetcode-cn.com/problems/palindrome-number/
class Solution:
    def isPalindrome2(self, x):
        num = 0
        y = x
        while y > 0:
            num = num * 10 + y % 10
            y //= 10
        return num == x
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x == y or x == y // 10
result = Solution().isPalindrome(1001) # True
print(result)
result = Solution().isPalindrome(121) # True
print(result)
result = Solution().isPalindrome(-121) # False
print(result)
result = Solution().isPalindrome(10) # False
print(result)
result = Solution().isPalindrome(0) # True
print(result)