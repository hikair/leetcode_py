# 找树左下角的值
# https://leetcode.cn/problems/find-bottom-left-tree-value/
from typing import Optional

from tree.treeNode import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        value, height = 0, 0

        def dfs(node, h):
            if not node:
                return
            h += 1
            dfs(node.left, h)
            dfs(node.right, h)
            nonlocal value, height
            if height < h:
                height = h
                value = node.val
        dfs(root, 0)
        return value


s = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert s.findBottomLeftValue(root) == 1
root.val = 1
l = TreeNode(2)
r = TreeNode(3)
root.left = l
root.right = r
l.left = TreeNode(4)
r.right = TreeNode(6)
rl = TreeNode(5)
r.left = rl
rl.left = TreeNode(7)
assert s.findBottomLeftValue(root) == 7
