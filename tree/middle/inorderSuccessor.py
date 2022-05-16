# 后继者
# https://leetcode.cn/problems/successor-lcci/
from collections import deque

from tree.treeNode import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = None
        if p.right:
            ans = p.right
            while ans.left:
                ans = ans.left
            return ans
        node = root
        while node:
            if node.val > p.val:
                ans = node
                node = node.left
            else:
                node = node.right
        return ans

    def inorderSuccessor2(self, root: TreeNode, p: TreeNode) -> TreeNode:
        q = deque()
        prev, cur = None, root
        while len(q) > 0 or cur is not None:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            if prev == p:
                return cur
            prev = cur
            cur = cur.right
