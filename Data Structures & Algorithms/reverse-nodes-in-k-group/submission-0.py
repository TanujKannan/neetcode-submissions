# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head

        while count < k:
            if temp is None:
                return head
            temp = temp.next
            count += 1
        
        prevNode = self.reverseKGroup(temp, k)

        count = 0
        temp = head
        while count < k:
            nxt = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = nxt
            count += 1
        
        return prevNode
        