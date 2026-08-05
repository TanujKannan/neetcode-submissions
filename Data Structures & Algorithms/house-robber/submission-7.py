class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        prevTwo = nums[0]
        prevOne = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(nums[i] + prevTwo, prevOne)
            print(cur)
            prevTwo = prevOne
            prevOne = cur
        
        return max(prevOne, prevTwo)
        