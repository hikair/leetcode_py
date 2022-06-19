# 出现次数最多的子树元素和
# https://leetcode.cn/problems/most-frequent-subtree-sum/
from collections import Counter
from typing import List

from tree.treeNode import TreeNode


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        c = Counter()

        def dfs(node):
            if not node:
                return 0
            sum = node.val + dfs(node.left) + dfs(node.right)
            c[sum] += 1
            return sum
        dfs(root)
        maxCount = max(c.values())
        return [i for i, j in c.items() if j == maxCount]


s = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)
print(s.findFrequentTreeSum(root)) # [2, -3, 4]
root.right = TreeNode(-5)
print(s.findFrequentTreeSum(root)) # [2]