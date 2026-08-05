'''
Need to return output where output[i] = prod of all nums except nums[i]

First idea to have a prefix and suffix array
prefix[i] = prod of all before i
suffix[i] = prod of all after i

then output[i] = prefix[i]*suffix[i]
O(N) space and time.

Might be able to do single array and do passes.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)

        suffix = [1]*len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        print(prefix)

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
    
        print(suffix)

        res = [1]*len(nums)

        for i in range(len(nums)):
            res[i] = prefix[i]*suffix[i]

        return res
