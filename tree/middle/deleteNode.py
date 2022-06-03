# 删除二叉搜索树中的节点
# https://leetcode.cn/problems/delete-node-in-a-bst/
from typing import Optional

from tree.treeNode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node, parent = root, None
        while node and node.val != key:
            parent = node
            node = node.left if node.val > key else node.right
        if not node:
            return root

        if node.left and node.right:
            # 找到前驱节点
            precursor, parent = node.left, node
            while precursor.right:
                parent = precursor
                precursor = precursor.right
            node.val = precursor.val
            precursor.val = key
            node = precursor
        if node.left:
            node = node.left
        else:
            node = node.right
        if not parent:
            return node

        if parent.left and parent.left.val == key:
            parent.left = node
        else:
            parent.right = node
        return root


def getTestRoot():
    root = TreeNode(5)
    l, r = TreeNode(3), TreeNode(6)
    l.left, l.right, r.right = TreeNode(2), TreeNode(4), TreeNode(7)
    root.left, root.right = l, r
    return root


s = Solution()
temp = s.deleteNode(getTestRoot(), 3)
assert temp.left.val == 2
assert temp.left.right.val == 4
assert not temp.left.left

temp = s.deleteNode(getTestRoot(), 5)
assert temp.val == 4
assert temp.left.val == 3
assert temp.left.left.val == 2
assert temp.right.val == 6
assert temp.right.right.val == 7

temp = s.deleteNode(getTestRoot(), 7)
assert temp.val == 5
assert temp.right.val == 6
assert not temp.right.right

root = TreeNode(1)
root.right = TreeNode(2)
temp = s.deleteNode(root, 1)
assert temp.val == 2