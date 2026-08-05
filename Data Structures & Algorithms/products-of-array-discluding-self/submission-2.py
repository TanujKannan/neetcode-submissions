class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n


        for i in range(1,n):
            output[i] = output[i-1] * nums[i-1]
        

        print(output)
        suffix = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
        