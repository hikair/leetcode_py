# 合并两个升序列表
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
result = s.mergeTwoLists(list1, list2)
while result != None:
    print(result.val)
    result = result.next
# [1, 1, 2, 3, 4, 4]