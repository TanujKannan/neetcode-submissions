from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def recurse(i, curSum):
            if i == n:
                if curSum == target:
                    return 1
                else:
                    return 0
            add = recurse(i + 1, curSum - nums[i])
            subtract = recurse(i+1, curSum + nums[i])

            return add + subtract
    
        return recurse(0 , 0)

        