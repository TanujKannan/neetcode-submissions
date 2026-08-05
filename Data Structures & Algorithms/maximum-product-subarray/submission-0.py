class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        if n < 2:
            return max(nums)
        maxProduct = nums[0]
        minProduct = nums[0]
        overall_max = nums[0]
        for x in nums[1:]:
            candidates = (x, x*minProduct, x*maxProduct)

            minProduct = min(candidates)
            maxProduct = max(candidates)

            overall_max = max(overall_max, maxProduct)
        
        return overall_max
        