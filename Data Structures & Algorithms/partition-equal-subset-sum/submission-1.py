from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum//2

        @cache
        def recurse(index, remaining):
            if remaining == 0:
                return True
            
            if remaining < 0:
                return False
            
            if index == n:
                return False
            
            take = recurse(index + 1, remaining - nums[index])
            skip = recurse(index + 1, remaining)

            return take or skip
        
        return recurse(0, target_sum)
        