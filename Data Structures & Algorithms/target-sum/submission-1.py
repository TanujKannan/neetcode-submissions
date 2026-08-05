from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def recurse(index, remaining):
            if index == n:
                if remaining == 0:
                    return 1
                else:
                    return 0
            
            add = recurse(index + 1, remaining - nums[index])
            subtract = recurse(index + 1, remaining + nums[index])
            return add + subtract
        
        return recurse(0, target)
        