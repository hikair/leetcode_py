# 电话号码的字母组合
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []

        def backtrack(conbination, next):
            if len(next) == 0:
                ans.append(conbination)
            else:
                for i in self.phone[next[0]]:
                    backtrack(conbination + i, next[1:])

        backtrack('', digits)
        return ans


s = Solution()
print(s.letterCombinations("23"))