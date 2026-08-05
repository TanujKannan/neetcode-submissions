class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robHouse(arr):
            if len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]
            prevTwo = arr[0]
            prevOne = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                cur = max(arr[i] + prevTwo, prevOne)
                prevTwo = prevOne
                prevOne = cur
            
            return max(prevTwo, prevOne)
        
        return max(robHouse(nums[1:]), robHouse(nums[:-1]))

        