# 删除排序链表中的重复元素
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head):
        temp = head
        while head is not None and head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return temp


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


s = Solution()
list = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
result = s.deleteDuplicates(list)
while result is not None:
    print(result.val)
    result = result.next
