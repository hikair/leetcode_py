# 删除最外层的括号
# https://leetcode.cn/problems/remove-outermost-parentheses/
from collections import deque


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, q = '', []
        for c in s:
            if c == ')':
                q.pop()
            if q:
                ans += c
            if c == '(':
                q.append(c)
        return ans


s = Solution()
assert s.removeOuterParentheses('(()())(())') == '()()()'
assert s.removeOuterParentheses('(()())(())(()(()))') == '()()()()(())'
assert s.removeOuterParentheses('()()') == ''
