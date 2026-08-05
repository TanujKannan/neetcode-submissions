class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Build prefix array first
        Then multiply the suffix as you go
        '''
        n = len(nums)
        prefix = [1]*n

        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]
        

        suffix = 1
        output = [0]*n
        for i in range(n-1, -1, -1):
            output[i] = prefix[i]*suffix
            suffix *= nums[i]
        
        return output
        