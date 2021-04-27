# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = node = head

        while node and node.next:
            next = node.next
            next.val, node.val = node.val, next.val
            node = node.next.next
        return root
