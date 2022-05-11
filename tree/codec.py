# 序列化和反序列化二叉搜索树
# https://leetcode.cn/problems/serialize-and-deserialize-bst/
from typing import List

from tree.treeNode import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return self.__preorderTraversal(root)[:-1]

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        return self.__deserialize(data.split(","))

    def __deserialize(self, data: List[str]):
        if not data:
            return None
        val = data[0]
        data.pop(0)
        if val == "#":
            return None
        root = TreeNode(int(val))
        root.left = self.__deserialize(data)
        root.right = self.__deserialize(data)
        return root

    def __preorderTraversal(self, root: TreeNode) -> str:
        if not root:
            return "#,"
        ans = str(root.val) + ","
        ans += self.__preorderTraversal(root.left)
        ans += self.__preorderTraversal(root.right)
        return ans


c = Codec()
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
root.left = node1
root.right = node2
node1.left = node4
node1.right = node5
node2.left = node3
print(c.serialize(root))
node = c.deserialize(c.serialize(root))
print(node)

