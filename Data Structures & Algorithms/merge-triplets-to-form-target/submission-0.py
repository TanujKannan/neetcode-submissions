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
        