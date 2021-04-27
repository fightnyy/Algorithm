from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lst : List = []
        tmp = head
        while tmp :
            lst = append(tmp.val)
            tmp = tmp.next
        tmp = head
        for v in lst:
            tmp.val = v
            tmp = tmp.next
        return head
        