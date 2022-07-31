# 最大层内元素和
# https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/
from typing import Optional

from tree.treeNode import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        nodes, ans, level, max_sum, = [root], 1, 1, root.val
        while nodes:
            sum, temp = 0, []
            for node in nodes:
                sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if sum > max_sum:
                ans, max_sum = level, sum
            level += 1
            nodes = temp
        return ans


s = Solution()
root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
assert s.maxLevelSum(root) == 2
root = TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, None, TreeNode(-32127))))
assert s.maxLevelSum(root) == 2