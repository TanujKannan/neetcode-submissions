'''
For every triplet, we are forced to pick the max.
So, when would it be impossible?
    1. If there is no triplet with elements <= each of elements of target.
Go through all triplets, skip over any where any element greater than target's elements.

If we can find a triplet, with even one > target, we skip
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a , b , c = target
        found_a = False
        found_b = False
        found_c = False

        for first, second, third in triplets:
            if first > a or second > b or third > c:
                continue

            if first == a:
                found_a = True
            
            if second == b:
                found_b = True
            
            if third == c:
                found_c = True
        
        return found_a and found_b and found_c

        