# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for index, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, index, head))
            
        dummy = ListNode(0)
        tail = dummy

        while heap:
            value, index, node = heapq.heappop(heap)
            tail.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
            tail = tail.next
    
        return dummy.next
        