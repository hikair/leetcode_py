# 在每个树行中找最大值
# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
from typing import List, Optional

from tree.treeNode import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        def dfs(node, height):
            if len(ans) == height:
                ans.append(node.val)
            else:
                ans[height] = max(ans[height], node.val)
            if node.left:
                dfs(node.left, height + 1)
            if node.right:
                dfs(node.right, height + 1)
        dfs(root, 0)
        return ans


s = Solution()
root = TreeNode(1,
                TreeNode(3, TreeNode(5), TreeNode(3)),
                TreeNode(2, None, TreeNode(9)))
l = s.largestValues(root)
assert l
assert len(l) == 3
assert l[0] == 1
assert l[1] == 3
assert l[2] == 9
