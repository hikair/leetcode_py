# 1171. 从链表中删去总和值为零的连续节点
# https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

from typing import Optional

from list.listNode import ListNode


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        sum, map = 0, dict()
        temp = dummy
        while temp:
            sum += temp.val
            map[sum] = temp
            temp = temp.next
        sum = 0
        temp = dummy
        while temp:
            sum += temp.val
            temp.next = map[sum].next
            temp = temp.next
        return dummy.next


s = Solution()
node = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2, ListNode(9))))))
s.removeZeroSumSublists(node)
