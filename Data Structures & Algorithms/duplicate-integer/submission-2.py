'''
Need to return true if any value appears more than once.
First Idea: Use a set since it doesn't store duplicates. Can just check the size. O(N) space and time.


'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)
    
        return False

        