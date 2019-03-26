"""
Reduce the assignment operations to speed up.
Runtime: 76 ms, faster than 100.00% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.3 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        pre = None
        carry = 0
        while (l1 or l2):
            if l1 is not None:
                x = l1.val
            else:
                x = 0
            if l2 is not None:
                y = l2.val
            else:
                y = 0
            z = x + y + carry
            if z<10:
                cur = ListNode(z)
                carry = 0
            else:
                cur = ListNode(z-10)
                carry = 1
            if head is None:
                head = cur
            else:
                pre.next = cur
            pre = cur
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return head
