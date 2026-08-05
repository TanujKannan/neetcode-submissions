class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        negProduct = nums[0]
        posProduct = nums[0]
        maxProduct = nums[0]


        for num in nums[1:]:
            neg = min(negProduct*num, posProduct*num, num)
            pos = max(negProduct*num, posProduct*num, num)

            negProduct = neg
            posProduct = pos
            maxProduct = max(maxProduct, posProduct)
        
        return maxProduct

        