class Solution:
    def rob(self, nums):
        n = len(nums)
        if n < 2:
            return max(nums)
        memo = {}
        def recurse(k):
            if k in memo:
                return memo[k]
            if k == 0:
                memo[0] = nums[0]
                return nums[0]
            if k == 1:
                memo[1] = max(nums[1], nums[0])
                return max(nums[1], nums[0])
            memo[k] = max(nums[k] + recurse(k-2), recurse(k-1))
            return max(nums[k] + recurse(k-2), recurse(k-1))
        return max(recurse(n-1), recurse(n-2))