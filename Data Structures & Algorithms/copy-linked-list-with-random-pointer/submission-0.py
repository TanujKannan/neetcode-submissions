"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        while curr:
            curr_copy = Node(curr.val)
            nxt = curr.next
            curr.next = curr_copy
            curr_copy.next = nxt
            curr = nxt
        
        curr = head
        while curr:
            copy_curr = curr.next
            if curr.random:
                copy_curr.random = curr.random.next
            curr = curr.next.next
        
        dummy = Node(0)
        copy_head = dummy
        curr = head

        while curr:
            copy = curr.next
            nxt_original = curr.next.next

            copy_head.next = copy
            copy_head = copy

            curr.next = nxt_original
            curr = curr.next
    
        return dummy.next

        


        