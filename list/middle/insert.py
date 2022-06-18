# 剑指 Offer II 029. 排序的循环链表
# https://leetcode.cn/problems/4ueAj6/
from list.node import Node


class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        no = Node(insertVal)
        if not head:
            head = no
            no.next = no
            return head
        if head == head.next:
            no.next = head
            head.next = no
            return head
        curr, ne = head, head.next
        while ne != head:
            if curr.val <= insertVal <= ne.val:
                break
            if curr.val > ne.val:
                if insertVal > curr.val or insertVal < ne.val:
                    break
            curr = curr.next
            ne = ne.next
        curr.next = no
        no.next = ne
        return head

