from functools import cache
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n < 2:
            return max(nums)
        dp = [0]*n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        print(dp)
        return max(dp[n-1], dp[n-2])