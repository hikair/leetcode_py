# 两两交换链表中的节点
# https://leetcode.cn/problems/swap-nodes-in-pairs/
from list.listNode import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyNode = ListNode(0, head)
        temp = dummyNode
        while temp.next and temp.next.next:
            l, r = temp.next, temp.next.next
            l.next, r.next = r.next, l
            temp.next = r
            temp = l
        return dummyNode.next


s = Solution()
t = s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
print(t)