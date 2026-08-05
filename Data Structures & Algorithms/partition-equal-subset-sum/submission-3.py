from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        n = len(nums)
        if totalSum % 2 == 1:
            return False
        
        target = totalSum // 2
        @cache
        def recurse(i , remaining):
            if i == n:
                return False
            
            if remaining == 0:
                return True
            
            take = recurse(i + 1, remaining - nums[i])
            skip = recurse(i+1, remaining)

            return take or skip
        
        return recurse(0, target)

        