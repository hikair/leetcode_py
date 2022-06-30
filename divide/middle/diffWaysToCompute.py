# 为运算表达式设计优先级
# https://leetcode.cn/problems/different-ways-to-add-parentheses/
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i, c in enumerate(expression):
            if c in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            ans.append(l + r)
                        elif c == '-':
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
        return ans


s = Solution()
print(s.diffWaysToCompute('2-1-1')) # [0,2]
print(s.diffWaysToCompute('2*3-4*5')) # [-34,-14,-10,-10,-10]