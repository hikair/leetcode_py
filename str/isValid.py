# 有效的括号
# https://leetcode-cn.com/problems/valid-parentheses/
class Solution:
    # 方法1
    def isValid2(self, s):
        stack = Stack()
        for i in s:
            if stack.isEmpty() == False and ord(i) - ord(stack.peek()) in [1, 2]:
                stack.pop()
            else:
                stack.push(i)
        return stack.isEmpty()

    # 方法2
    def isValid(self, s):
        stack = []
        for i in s:
            if stack and stack[-1] + i in ['()', '[]', '{}']:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

s = Solution()
print(s.isValid('"(){}}{"')) # False
print(s.isValid('((')) # False
print(s.isValid('()')) # True
print(s.isValid('()[]{}')) # True
print(s.isValid('(]')) # False
print(s.isValid('([)]')) # False
print(s.isValid('{[]}')) # True

