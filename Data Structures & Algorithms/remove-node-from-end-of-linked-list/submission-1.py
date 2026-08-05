# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        dummy = ListNode(0)
        dummy.next = head
        second = dummy

        iteration = 0
        while iteration < n:
            first = first.next
            iteration += 1
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next
        