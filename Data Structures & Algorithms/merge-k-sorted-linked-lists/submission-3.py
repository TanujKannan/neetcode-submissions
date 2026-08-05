# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            dummy = ListNode(0)
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                elif l2.val < l1.val:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            
            return dummy.next
        
        num_lists = len(lists)
        radius = 1

        while radius < num_lists:
            for i in range(0 , num_lists - radius, 2*radius):
                lists[i] = merge2Lists(lists[i], lists[i + radius])
            radius *= 2
        
        return lists[0] if num_lists > 0 else None

        