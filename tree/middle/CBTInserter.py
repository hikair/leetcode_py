# 完全二叉树插入器
# https://leetcode.cn/problems/complete-binary-tree-inserter/
from collections import deque

from tree.treeNode import TreeNode


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = deque()
        self.__init_queue()

    def insert(self, val: int) -> int:
        child, node = TreeNode(val), self.queue[0]
        ans = node.val
        if not node.left:
            node.left = child
        else:
            node.right = child
            self.queue.popleft()
        self.queue.append(child)
        return ans

    def get_root(self) -> TreeNode:
        return self.root

    def __init_queue(self):
        temp = deque([self.root])
        while temp:
            node = temp.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not node.left or not node.right:
                self.queue.append(node)


root = TreeNode(1,
                TreeNode(2, TreeNode(4, TreeNode(8, None)), TreeNode(5)),
                TreeNode(3, TreeNode(6, TreeNode(7))))
c = CBTInserter(root)
assert c.insert(9) == 4