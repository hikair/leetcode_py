# 1302. 层数最深叶子节点的和
from collections import deque
from typing import Optional

from tree.treeNode import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans, queue = 0, deque()
        queue.append(root)
        while queue:
            ans, size = 0, len(queue)
            for _ in range(size):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


s = Solution()
root = TreeNode(1,
                TreeNode(2, TreeNode(4, TreeNode(7), None), TreeNode(5)),
                TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
assert s.deepestLeavesSum(root) == 15