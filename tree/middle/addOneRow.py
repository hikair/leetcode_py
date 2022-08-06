# 在二叉树中增加一行
# https://leetcode.cn/problems/add-one-row-to-tree/
from typing import Optional

from tree.treeNode import TreeNode


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        if depth == 2:
            root.left = TreeNode(val, root.left)
            root.right = TreeNode(val, None, root.right)
        else:
            if root.left:
                root.left = self.addOneRow(root.left, val, depth - 1)
            if root.right:
                root.right = self.addOneRow(root.right, val, depth - 1)
        return root


s = Solution()
# root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
# node = s.addOneRow(root, 1, 2)
# print(node)
# root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
# node = s.addOneRow(root, 1, 3)
# print(node)
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
node = s.addOneRow(root, 5, 4)
print(node)