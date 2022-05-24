# 单值二叉树
# https://leetcode.cn/problems/univalued-binary-tree/
from collections import deque

from tree.treeNode import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        num = root.val
        q = deque()
        temp = root
        while temp:
            if num != temp.val:
                return False
            q.append(temp)
            temp = temp.left
        while len(q) > 0:
            node = q.pop()
            temp = node.right
            while temp:
                if num != temp.val:
                    return False
                q.append(temp)
                temp = temp.left
        return True


s = Solution()
root = TreeNode(5)
r1 = TreeNode(5)
root.right = r1
l2 = TreeNode(5)
r1.left = l2
r2 = TreeNode(5)
r1.right = r2
r3 = TreeNode(0)
l2.right = r3
assert s.isUnivalTree(root) == False