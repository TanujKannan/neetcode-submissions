'''
At any index, I either include nums[i] or I don't.
That's two choices.

If I include, then length increases by 1.
If I don't

Do I only need to keep track of index?




'''
from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def recurse(i):
            curMax = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    internal = recurse(j)
                    curMax = max(curMax, internal + 1)
            return curMax
        
        return max(recurse(i) for i in range(n))
            

        