# 二叉树剪枝
# https://leetcode.cn/problems/binary-tree-pruning/
from typing import Optional

from tree.treeNode import TreeNode


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            if dfs(node.left):
                node.left = None
            if dfs(node.right):
                node.right = None
            return node.val == 0 and not node.left and not node.right
        return None if dfs(root) else root


s = Solution()
node1 = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
node1 = s.pruneTree(node1)
node2 = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
node2 = s.pruneTree(node2)
print()