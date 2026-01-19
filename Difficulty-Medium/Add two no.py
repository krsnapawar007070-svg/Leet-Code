# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0

        p, q = l1, l2

        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0

            total = carry + x + y
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if p:
                p = p.next
            if q:
                q = q.next

        if carry:
            current.next = ListNode(carry)

        return dummyHead.next
