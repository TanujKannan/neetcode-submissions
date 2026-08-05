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

        #Interleave the copies
        curr = head
        while curr:
            copy = Node(curr.val)
            nxt = curr.next
            curr.next = copy
            copy.next = nxt
            curr = nxt

        #Add the random connections
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = curr.next.next
        
        dummy = Node(0)
        copy_tail = dummy
        curr = head

        while curr:
            copy = curr.next
            nxt_original = copy.next

            copy_tail.next = copy
            copy_tail = copy

            curr.next = nxt_original
            curr = nxt_original
        
        return dummy.next

        

        

        