class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        prevOne = nums[0]
        prevTwo = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(nums[i] + prevOne, prevTwo)
            print(cur)
            prevOne = prevTwo
            prevTwo = cur
        
        return max(prevOne, prevTwo)
        