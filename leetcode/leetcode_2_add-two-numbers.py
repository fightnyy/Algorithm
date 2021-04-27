# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        cin = 0
        while l1 or l2 or cin == 1:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            sum += cin

            cin, v = divmod(sum, 10)

            head.next = ListNode(v)
            head = head.next

        return root.next
