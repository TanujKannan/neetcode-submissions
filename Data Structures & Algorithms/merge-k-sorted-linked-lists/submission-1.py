# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            dummy = ListNode(0)
            curr = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                elif l2.val < l1.val:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            if l1:
                curr.next = l1
            
            if l2:
                curr.next = l2
            
            return dummy.next
        total_lists = len(lists)
        radius = 1
        while radius < total_lists:
            for i in range(0, total_lists - radius, 2*radius):
                lists[i] = merge2Lists(lists[i], lists[i+radius])
            radius *= 2
        
        return lists[0] if total_lists > 0 else None
        