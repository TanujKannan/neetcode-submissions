from functools import cache
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n < 2:
            return max(nums)
        @cache
        def recurse(k):
            if k == 0:
                return nums[0]
            if k == 1:
                return max(nums[1], nums[0])
            return max(nums[k] + recurse(k-2), recurse(k-1))
        return max(recurse(n-1), recurse(n-2))